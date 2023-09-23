from entidad_con_sprite import Entidad_con_sprite
from animacion import Animacion
import herramientas_imagen as hi
import numpy as np

class Jugador(Entidad_con_sprite):
    def __init__(self, controles):
        super().__init__(pos_x=0, pos_y=0, offset_x=0, offset_y=0, tam_x=16, tam_y=16, velocidad=3)
        self.controles = controles
        self.cargar_animaciones()
          
    def cargar_animaciones(self):
        self.agregar_animaciones(["andar_abajo", "andar_arriba", "andar_izquierda", "andar_derecha"],"res/Actor/Characters/Boy/SeparateAnim/Walk.png")
        self.agregar_animaciones(["idle_abajo", "idle_arriba", "idle_izquierda", "idle_derecha"], "res/Actor/Characters/Boy/SeparateAnim/Idle.png")
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
        