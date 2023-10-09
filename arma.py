from entidad_con_sprite import Entidad_con_sprite
import herramientas_imagen as hi
from animacion import Animacion
from ajustes import *

class Arma(Entidad_con_sprite):
    def __init__(self, jugador, tam_x, tam_y):
        super().__init__(jugador.pos_x, jugador.pos_y, jugador.offset_x, jugador.offset_y, tam_x, tam_y, velocidad=0, mapa=None)
        self.jugador = jugador
        
    def cargar_animaciones(self):
        
        ruta = "res/Items/Weapons/Katana/Sprite.png"
        
        self.agregar_animacion("atacar_derecha", Animacion( hi.redimensionar_imagenes( hi.generar_frames_animacion_rotacion(ruta, 90, 180, 20), ESCALA_ZOOM ) ))
        self.cambiar_animacion("atacar_derecha")