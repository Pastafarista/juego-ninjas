import pygame

#Clase que gestiona los inputs del usuario
class Controles:
    def __init__(self):
        self.controles_cooldown = {"w":False,"a":False,"d":False,"s":False,"f":False,"r":False,"g":False}
        
        #Diccionario que relaciona todas las teclas con su tecla de pygame
        self.nombre_controles = {"w":pygame.K_w,"a":pygame.K_a,"d":pygame.K_d,"s":pygame.K_s,"f":pygame.K_f,"r":pygame.K_r,"g":pygame.K_g}
        
    def obtener_tecla(self,tecla):
        key = pygame.key.get_pressed()
        
        if key[self.nombre_controles[tecla]]:
            return True
        else:
            return False

    def obtener_tecla_con_cooldown(self,tecla):
        if self.obtener_tecla(tecla) and self.controles_cooldown[tecla] == False:
            self.controles_cooldown[tecla] = True
            return True
        elif self.obtener_tecla(tecla) == False:
            self.controles_cooldown[tecla] = False
            return False