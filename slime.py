from entidad_con_sprite import Entidad_con_sprite
from animacion import Animacion
from timer import Timer
from random import randint
import numpy as np

class Slime(Entidad_con_sprite):
    def __init__(self, pos_x, pos_y, mapa):
        super().__init__(pos_x, pos_y, 0, 0, 12, 12 , 1, mapa)

        self.timer_cooldown_moverse = Timer()
        self.direccion_actual = np.array([0, 0])
        self.cargar_animaciones()
        
    def cargar_animaciones(self):
        
        nombres_animaciones = ["andar_abajo", "andar_arriba", "andar_izquierda", "andar_derecha"]
        
        self.agregar_animaciones(nombres_animaciones, "res/Actor/Monsters/Slime.png")
        
        self.cambiar_animacion("andar_abajo")
            
    def actualizar_estado(self):      
        
        estado = self.nombre_animacion_actual
        
        if self.direccion[0] > 0 and self.direccion[0] > self.direccion[1]:
            estado = "andar_derecha"
        elif self.direccion[0] < 0 and self.direccion[0] < self.direccion[1]:
            estado = "andar_izquierda"
        elif self.direccion[1] > 0 and self.direccion[1] > self.direccion[0]:
            estado = "andar_abajo"
        elif self.direccion[1] < 0 and self.direccion[1] < self.direccion[0]:
            estado = "andar_arriba"
            
        self.cambiar_animacion(estado)
        
    def inteligencia_artifical_slime(self):
        
        #Cambiar la dirección actual cada 3-5 segundos
        if self.timer_cooldown_moverse.activado == False:
            
            self.direccion_actual = np.array([0, 0])
            
            #Cambiar a una dirección aleatorio pero que no es diagonal
            if randint(0, 1) == 0:
                self.direccion_actual[0] = randint(-1, 1)
            else:
                self.direccion_actual[1] = randint(-1, 1)
            
            self.timer_cooldown_moverse.activar(randint(1, 3))
            
        self.direccion = self.direccion_actual
            
    def actualizar(self):
        super().actualizar()
        self.timer_cooldown_moverse.actualizar()
        self.inteligencia_artifical_slime()
        self.actualizar_estado()