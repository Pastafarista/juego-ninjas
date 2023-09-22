import pygame
from entidad import Entidad
from animacion import Animacion

class Entidad_con_sprite(Entidad):
    def __init__(self, pos_x, pos_y, offset_x, offset_y, tam_x, tam_y, velocidad):
        super().__init__(pos_x, pos_y, offset_x, offset_y, tam_x, tam_y, velocidad)
        self.animacion_actual = ""     
        self.animaciones = {}
        
    def agregar_animacion(self, nombre, imagenes):
        self.animaciones[nombre] = Animacion(imagenes)
        
    def cambiar_animacion(self, nombre):
        self.animacion_actual = nombre
        self.animaciones[self.animacion_actual].reiniciar()
        
    def actualizar(self):
        super().actualizar()
        self.animaciones[self.animacion_actual].siguiente_frame()