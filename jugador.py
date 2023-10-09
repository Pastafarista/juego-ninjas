from entidad import Entidad
from controles import Controles
from arma import Arma
import numpy as np
from sprite import Sprite

class Jugador(Entidad):
    def __init__(self, mapa):
        super().__init__(pos_x=200, pos_y=200, offset_x=2, offset_y=3, tam_x=11, tam_y=11, velocidad=2 * 60, mapa=mapa)
        self.controles = Controles()
        self.vida = 12
        self.vida_maxima = 12
        self.sprite = Sprite()
        self.arma = Arma(self)
        self.direccion_texto = "abajo"
        self.añadir_timer("cooldown_vida")
        self.añadir_timer("cooldown_ataque")
        self.cargar_animaciones("BlueNinja")
          
    def cargar_animaciones(self, nombre_skin):
        self.sprite.agregar_animaciones(["andar_abajo", "andar_arriba", "andar_izquierda", "andar_derecha"],"res/Actor/Characters/" + nombre_skin + "/SeparateAnim/Walk.png")
        self.sprite.agregar_animaciones(["idle_abajo", "idle_arriba", "idle_izquierda", "idle_derecha"], "res/Actor/Characters/" +  nombre_skin + "/SeparateAnim/Idle.png")
        self.sprite.agregar_animaciones(["atacar_abajo", "atacar_arriba", "atacar_izquierda", "atacar_derecha"], "res/Actor/Characters/" +  nombre_skin + "/SeparateAnim/Attack.png")
        self.sprite.cambiar_animacion("idle_abajo")
            
    def comprobar_teleports(self):
        for teleport in self.mapa.objetos["teleport"]:
            if self.caja_colision.colliderect(teleport.caja_colision):
                self.mapa.entidades.remove(self)
                
                self.mapa = self.mapa.mundo.mapas[teleport.nombre_mapa_destino]
                self.mapa.entidades.append(self)
                
                #Cambiar la posición del jugador
                self.pos_x_real = teleport.destino_x
                self.pos_y_real = teleport.destino_y
                self.actualizar_hitbox()
    
    #Comprobar si el jugador está colisionando con algún enemigo y restarle vida           
    def comprobar_colisiones_enemigos(self):
        if(self.timers["cooldown_vida"].activado == False):
            for enemigo in self.mapa.enemigos:
                if self.caja_colision.colliderect(enemigo.caja_colision):
                    self.vida -= enemigo.daño
                    self.desplazarse(-self.obtener_ultima_direccion(), 0.25)       
                    self.timers["cooldown_vida"].activar(1)

    def obtener_ultima_direccion(self):
        if self.direccion_texto == "abajo":
            return np.array([0, 1])
        elif self.direccion_texto == "arriba":
            return np.array([0, -1])
        elif self.direccion_texto == "izquierda":
            return np.array([-1, 0])
        elif self.direccion_texto == "derecha":
            return np.array([1, 0])

    def actualizar_estado(self):    
        #Si se está desplazando, no se puede cambiar de dirección
        if self.se_esta_desplazando() == True:
            return
        
        self.direccion = np.array([0, 0])
        
        estado = self.sprite.nombre_animacion_actual    
        
        if self.controles.obtener_tecla_con_cooldown("espacio") and self.timers["cooldown_ataque"].activado == False:
            estado = "atacar_" + self.direccion_texto
            self.timers["cooldown_ataque"].activar(0.1)
            # Parar al personaje en seco
            self.direccion[0] = 0
            self.direccion[1] = 0
        
        if self.timers["cooldown_ataque"].activado == False: # Solo va a poder andar si no está atacando
            if self.controles.obtener_tecla("w"):
                self.direccion_texto = "arriba"
                self.direccion[1] += -1
                
            if self.controles.obtener_tecla("a"):
                self.direccion_texto = "izquierda"
                self.direccion[0] += -1
                
            if self.controles.obtener_tecla("s"):
                self.direccion_texto = "abajo"
                self.direccion[1] += 1
                
            if self.controles.obtener_tecla("d"):
                self.direccion_texto = "derecha"
                self.direccion[0] += 1
            
            #Cambiar la animación a idle si no se está moviendo   
            if self.direccion[0] == 0 and self.direccion[1] == 0:
                estado = "atacar_" + self.direccion_texto
            else:
                estado = "andar_" + self.direccion_texto
        
        self.sprite.cambiar_animacion(estado)
        
    def actualizar(self, dt):
        super().actualizar(dt)
        self.sprite.actualizar(dt)
        self.arma.actualizar(dt)
        self.comprobar_colisiones_enemigos()
        self.actualizar_estado()
        self.comprobar_teleports()
        