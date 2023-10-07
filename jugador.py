from entidad_con_sprite import Entidad_con_sprite
from controles import Controles
from timer import Timer
import numpy as np

class Jugador(Entidad_con_sprite):
    def __init__(self, mapa):
        super().__init__(pos_x=200, pos_y=200, offset_x=2, offset_y=3, tam_x=11, tam_y=11, velocidad=2, mapa=mapa)
        self.controles = Controles()
        self.cargar_animaciones("BlueNinja")
        self.vida = 12
        self.vida_maxima = 12
        self.añadir_timer("cooldown_vida")
          
    def cargar_animaciones(self, nombre_skin):
        self.agregar_animaciones(["andar_abajo", "andar_arriba", "andar_izquierda", "andar_derecha"],"res/Actor/Characters/" + nombre_skin + "/SeparateAnim/Walk.png")
        self.agregar_animaciones(["idle_abajo", "idle_arriba", "idle_izquierda", "idle_derecha"], "res/Actor/Characters/" +  nombre_skin + "/SeparateAnim/Idle.png")
        self.cambiar_animacion("idle_abajo")
            
    def comprobar_teleports(self):
        for teleport in self.mapa.objetos["teleport"]:
            if self.caja_colision.colliderect(teleport.caja_colision):
                self.mapa.entidades.remove(self)
                
                self.mapa = self.mapa.mundo.mapas[teleport.nombre_mapa_destino]
                self.mapa.entidades.append(self)
                
                #Cambiar la posición del jugador
                self.posicion[0] = teleport.destino_x
                self.posicion[1] = teleport.destino_y
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
        texto_direccion = self.nombre_animacion_actual.split("_")[1]
        
        if texto_direccion == "abajo":
            return np.array([0, 1])
        elif texto_direccion == "arriba":
            return np.array([0, -1])
        elif texto_direccion == "izquierda":
            return np.array([-1, 0])
        elif texto_direccion == "derecha":
            return np.array([1, 0])

    def actualizar_estado(self):    
        #Si se está desplazando, no se puede cambiar de dirección
        if self.se_esta_desplazando() == True:
            return
        
        self.direccion = np.array([0, 0])
        
        estado = self.nombre_animacion_actual
        
        if self.controles.obtener_tecla("w"):
            estado = "andar_arriba"
            self.direccion[1] += -1
            
        if self.controles.obtener_tecla("a"):
            estado = "andar_izquierda"
            self.direccion[0] += -1
            
        if self.controles.obtener_tecla("s"):
            estado = "andar_abajo"
            self.direccion[1] += 1
            
        if self.controles.obtener_tecla("d"):
            estado = "andar_derecha"
            self.direccion[0] += 1
        
        #Cambiar la animación a idle si no se está moviendo   
        if self.direccion[0] == 0 and self.direccion[1] == 0:
            estado = "idle_" + estado.split("_")[1]
        
        self.cambiar_animacion(estado)
        
    def actualizar(self):
        super().actualizar()
        self.comprobar_colisiones_enemigos()
        self.actualizar_estado()
        self.comprobar_teleports()
        print(self.posicion)
        