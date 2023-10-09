from entidad import Entidad
from sprite import Sprite
from timer import Timer
from random import randint
import numpy as np

class Slime(Entidad):
    def __init__(self, pos_x, pos_y, mapa):
        super().__init__(pos_x=pos_x, pos_y=pos_y, offset_x=3, offset_y=4, tam_x=11, tam_y=9, velocidad=60, mapa=mapa)

        self.daño = 1
        self.direccion_actual = np.array([0, 0])
        self.sprite = Sprite()
        self.cargar_animaciones()
        
    def cargar_animaciones(self):
        
        nombres_animaciones = ["andar_abajo", "andar_arriba", "andar_izquierda", "andar_derecha"]
        
        self.sprite.agregar_animaciones(nombres_animaciones, "res/Actor/Monsters/Slime2.png")
        
        self.sprite.cambiar_animacion("andar_abajo")
            
    def actualizar_estado(self):      
        
        estado = self.sprite.nombre_animacion_actual
        
        if self.direccion[0] > 0 and self.direccion[0] > self.direccion[1]:
            estado = "andar_derecha"
        elif self.direccion[0] < 0 and self.direccion[0] < self.direccion[1]:
            estado = "andar_izquierda"
        elif self.direccion[1] > 0 and self.direccion[1] > self.direccion[0]:
            estado = "andar_abajo"
        elif self.direccion[1] < 0 and self.direccion[1] < self.direccion[0]:
            estado = "andar_arriba"
            
        self.sprite.cambiar_animacion(estado)
        
    def inteligencia_artifical_slime(self):   
        #Cambiar la dirección actual cada 3-5 segundos
        if self.se_esta_desplazando() == False:
            self.direccion_actual = np.array([0, 0])
            
            #Cambiar a una dirección aleatorio pero que no es diagonal
            if randint(0, 1) == 0:
                self.direccion_actual[0] = randint(-1, 1)
            else:
                self.direccion_actual[1] = randint(-1, 1)
            
            self.desplazarse(self.direccion_actual, randint(1, 3))
            
    def actualizar(self, dt):
        super().actualizar(dt)
        self.sprite.actualizar(dt)
        self.inteligencia_artifical_slime()
        self.actualizar_estado()