from sprite import Sprite
import herramientas_imagen as hi
from animacion import Animacion
from ajustes import *

class Arma(Sprite):
    def __init__(self, jugador):
        self.jugador = jugador
        self.pos_x = jugador.pos_x
        self.pos_y = jugador.pos_y
        self.sprite = Sprite()
        self.offsets = {
            "derecha":(7, 11),
            "izquierda":(-5, 11),
            "arriba":(10, -5),
            "abajo":(0, 14)
        }
        self.cargar_animaciones()
        
    def cargar_animaciones(self):
        
        ruta = "res/Items/Weapons/Katana/Sprite.png"
        
        dict = {
            "derecha":270,
            "izquierda":90,
            "arriba":0,
            "abajo":180
        }
        
        for direccion, rotacion in dict.items():
            self.sprite.agregar_animacion("idle_" + direccion, Animacion( [hi.redimensionar_imagen(hi.rotar_imagen(hi.cargar_imagen(ruta), rotacion), ESCALA_ZOOM)] ) )
                   
        self.sprite.cambiar_animacion("idle_abajo")
        
    def actualizar_estado(self):
        direccion = self.jugador.sprite.nombre_animacion_actual.split("_")[-1]
        estado = "idle"
        self.sprite.cambiar_animacion(estado + "_" + direccion)
        
        # Hay que cambiar la capa para que visualmente se vea bien
        if(direccion != "arriba"):
            self.sprite.capa = self.jugador.sprite.capa
        else:
            self.sprite.capa = self.jugador.sprite.capa - 1
        
    def actualizar(self, dt):
        self.actualizar_estado()
        self.sprite.actualizar(dt)
        self.pos_x = self.jugador.pos_x + self.offsets[self.jugador.sprite.nombre_animacion_actual.split("_")[-1]][0]
        self.pos_y = self.jugador.pos_y + self.offsets[self.jugador.sprite.nombre_animacion_actual.split("_")[-1]][1]
