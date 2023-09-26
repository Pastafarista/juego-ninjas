from entidad import Entidad
from animacion import Animacion
import herramientas_imagen as hi
from ajustes import *

class Entidad_con_sprite(Entidad):
    def __init__(self, pos_x, pos_y, offset_x, offset_y, tam_x, tam_y, velocidad, mapa):
        super().__init__(pos_x, pos_y, offset_x, offset_y, tam_x, tam_y, velocidad, mapa)
        self.animacion_actual = ""     
        self.animaciones = {}     
        self.capa = 2
        
    def agregar_animacion(self, nombre, animacion):
        self.animaciones[nombre] = animacion
        
    def agregar_animaciones(self, nombres, ruta_spritesheet):
        indice = 0

        for imagenes in hi.cargar_spritesheet_animacion_por_columnas(ruta_spritesheet):
            animacion = Animacion(hi.redimensionar_imagenes(imagenes, ESCALA_ZOOM))
            self.agregar_animacion(nombres[indice], animacion)
            indice += 1
        
    def cambiar_animacion(self, nombre):
        if nombre != self.animacion_actual:
            self.animacion_actual = nombre
            self.animaciones[self.animacion_actual].reiniciar()
        
    def actualizar(self):
        super().actualizar()
        self.animaciones[self.animacion_actual].siguiente_frame()
        
    def obtener_frame_actual(self):
        return self.animaciones[self.animacion_actual].obtener_frame_actual()