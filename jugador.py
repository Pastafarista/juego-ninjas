from entidad_con_sprite import Entidad_con_sprite
from controles import Controles
import numpy as np

class Jugador(Entidad_con_sprite):
    def __init__(self, mapa):
        super().__init__(pos_x=200, pos_y=200, offset_x=2, offset_y=3, tam_x=11, tam_y=11, velocidad=2, mapa=mapa)
        self.controles = Controles()
        self.cargar_animaciones("BlueNinja")
          
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

            
    def actualizar_estado(self):
        
        self.direccion = np.array([0, 0])
        
        estado = self.animacion_actual
        
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
        self.actualizar_estado()
        self.comprobar_teleports()
        print(self.posicion)
        