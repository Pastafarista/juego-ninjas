from entidad import Entidad
from animacion import Animacion
import herramientas_imagen as hi
from ajustes import *

class Sprite(Entidad):
    def __init__(self,):
        self.nombre_animacion_actual = ""     
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
        if nombre != self.nombre_animacion_actual:
            self.nombre_animacion_actual = nombre
            self.animaciones[self.nombre_animacion_actual].reiniciar()
        
    def cambiar_animacion_sin_reiniciar(self, nombre):
        if nombre != self.nombre_animacion_actual:
            self.nombre_animacion_actual = nombre
        
    def actualizar(self, dt):
        self.animaciones[self.nombre_animacion_actual].siguiente_frame(dt)
        
    def obtener_frame_actual(self):
        return self.animaciones[self.nombre_animacion_actual].obtener_frame_actual()