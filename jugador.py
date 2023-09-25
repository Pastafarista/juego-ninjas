from entidad_con_sprite import Entidad_con_sprite
from animacion import Animacion
from camara import Camara
import herramientas_imagen as hi
import numpy as np

class Jugador(Entidad_con_sprite):
    def __init__(self, controles, mapa):
        super().__init__(pos_x=0, pos_y=0, offset_x=0, offset_y=0, tam_x=16, tam_y=16, velocidad=2, mapa=mapa)
        self.controles = controles
        self.cargar_animaciones("BlueNinja")
          
    def cargar_animaciones(self, nombre_skin):
        self.agregar_animaciones(["andar_abajo", "andar_arriba", "andar_izquierda", "andar_derecha"],"res/Actor/Characters/" + nombre_skin + "/SeparateAnim/Walk.png")
        self.agregar_animaciones(["idle_abajo", "idle_arriba", "idle_izquierda", "idle_derecha"], "res/Actor/Characters/" +  nombre_skin + "/SeparateAnim/Idle.png")
        self.cambiar_animacion("idle_abajo")
            
    def actualizar(self):
        
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
        
        super().actualizar()
        