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
            "derecha":(16, 9),
            "izquierda":(-10, 9),
            "arriba":(2, -10),
            "abajo":(3, 16)
        }
        self.cargar_animaciones()
        
    def cargar_animaciones(self):
        
        ruta = "res/Items/Weapons/Katana/SpriteInHand.png"
        
        dict = {
            "derecha":90,
            "izquierda":270,
            "arriba":180,
            "abajo":0
        }

        self.sprite.agregar_animacion("idle_derecha", Animacion( [hi.redimensionar_imagen(hi.rotar_imagen( hi.flip_imagen( hi.cargar_imagen(ruta), flip_x=False, flip_y=False ), dict["derecha"]), ESCALA_ZOOM)] ) )
        self.sprite.agregar_animacion("idle_arriba", Animacion( [hi.redimensionar_imagen(hi.rotar_imagen( hi.flip_imagen( hi.cargar_imagen(ruta), flip_x=False, flip_y=False ), dict["arriba"]), ESCALA_ZOOM)] ) )       
        self.sprite.agregar_animacion("idle_izquierda", Animacion( [hi.redimensionar_imagen(hi.rotar_imagen( hi.flip_imagen( hi.cargar_imagen(ruta), flip_x=True, flip_y=False ), dict["izquierda"]), ESCALA_ZOOM)] ) )
        self.sprite.agregar_animacion("idle_abajo", Animacion( [hi.redimensionar_imagen(hi.rotar_imagen( hi.flip_imagen( hi.cargar_imagen(ruta), flip_x=False, flip_y=False ), dict["abajo"]), ESCALA_ZOOM)] ) )

        self.sprite.cambiar_animacion("idle_abajo")
        
    def actualizar_estado(self):
        direccion = self.jugador.sprite.nombre_animacion_actual.split("_")[-1]
        estado = "idle"
        self.sprite.cambiar_animacion(estado + "_" + direccion)
        
    def actualizar(self, dt):
        self.actualizar_estado()
        self.sprite.actualizar(dt)
        self.pos_x = self.jugador.pos_x + self.offsets[self.jugador.sprite.nombre_animacion_actual.split("_")[-1]][0]
        self.pos_y = self.jugador.pos_y + self.offsets[self.jugador.sprite.nombre_animacion_actual.split("_")[-1]][1]
