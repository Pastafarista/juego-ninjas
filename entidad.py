import numpy as np 
import math
import pygame

class Entidad:
    def __init__(self, pos_x, pos_y, offset_x, offset_y, tam_x, tam_y, velocidad, mapa):
        self.posicion = np.array([pos_x, pos_y], dtype=float)
        self.caja_colision = pygame.Rect(offset_x, offset_y, tam_x, tam_y)
        self.velocidad = velocidad
        self.direccion = np.array([0, 0], dtype=float)
        self.tam_x = tam_x
        self.tam_y = tam_y
        self.mapa = mapa
    
    def moverse(self):  
        
        #Normalizar la dirección
        if(self.direccion[0] != 0 and self.direccion[1] != 0):
            self.direccion = self.direccion / np.sqrt(np.sum(self.direccion**2))
            
        self.posicion += self.direccion * self.velocidad
    
    def actualizar(self):
        self.moverse()