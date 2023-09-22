from entidad_con_sprite import Entidad_con_sprite
from animacion import Animacion
import herramientas_imagen as hi

class Jugador(Entidad_con_sprite):
    def __init__(self, controles):
        super().__init__(pos_x=0, pos_y=0, offset_x=0, offset_y=0, tam_x=16, tam_y=16, velocidad=2)
        self.controles = controles
        self.teclas_cooldown = {"w":False,"a":False,"d":False,"s":False,"f":False,"r":False,"g":False}
        self.cargar_animaciones()
        
    def cargar_animaciones(self):
        nombres = ["andar_abajo", "andar_arriba", "andar_izquierda", "andar_derecha"]
        indice = 0

        for columna in hi.cargar_spritesheet_por_columnas("res/Actor/Characters/Boy/SeparateAnim/Walk.png"):
            animacion = Animacion(hi.redimensionar_imagenes(columna, 5))
            self.agregar_animacion(nombres[indice], animacion)
            indice += 1
            
        self.cambiar_animacion("andar_abajo")
           
    def obtener_tecla_cooldown(self, tecla):
        if self.controles.obtener_tecla(tecla) and self.teclas_cooldown[tecla] == False:
            self.cambiar_animacion("andar_arriba")
            self.teclas_cooldown[tecla] = True
            return True
        elif self.controles.obtener_tecla(tecla) == False:
            self.teclas_cooldown[tecla] = False
            return False
            
    def actualizar(self):
        super().actualizar()
        
        if self.obtener_tecla_cooldown("w"):
            self.cambiar_animacion("andar_arriba")
            
        if self.obtener_tecla_cooldown("a"):
            self.cambiar_animacion("andar_izquierda")
            
        if self.obtener_tecla_cooldown("s"):
            self.cambiar_animacion("andar_abajo")
            
        if self.obtener_tecla_cooldown("d"):
            self.cambiar_animacion("andar_derecha")
        
            
        