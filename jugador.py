from entidad_con_sprite import Entidad_con_sprite
from animacion import Animacion
import herramientas_imagen as hi

class Jugador(Entidad_con_sprite):
    def __init__(self, controles):
        super().__init__(pos_x=0, pos_y=0, offset_x=0, offset_y=0, tam_x=16, tam_y=16, velocidad=2)
        self.controles = controles
        self.cargar_animaciones()
        
    def cargar_animaciones(self):
        nombres = ["andar_abajo", "andar_arriba", "andar_izquierda", "andar_derecha"]
        indice = 0

        for columna in hi.cargar_spritesheet_por_columnas("res/Actor/Characters/Boy/SeparateAnim/Walk.png"):
            animacion = Animacion(hi.redimensionar_imagenes(columna, 5))
            self.agregar_animacion(nombres[indice], animacion)
            indice += 1
            
        self.cambiar_animacion("andar_abajo")
            
    def actualizar(self):
        super().actualizar()
        
        if self.controles.obtener_tecla_con_cooldown("w"):
            self.cambiar_animacion("andar_arriba")
            
        if self.controles.obtener_tecla_con_cooldown("a"):
            self.cambiar_animacion("andar_izquierda")
            
        if self.controles.obtener_tecla_con_cooldown("s"):
            self.cambiar_animacion("andar_abajo")
            
        if self.controles.obtener_tecla_con_cooldown("d"):
            self.cambiar_animacion("andar_derecha")
        
            
        