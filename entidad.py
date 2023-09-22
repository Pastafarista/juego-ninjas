import numpy as np 
import pygame

class entidad:
    def __init__(self, pos_x, pos_y, tam_x, tam_y, velocidad):
        self.posicion = np.array([pos_x, pos_y])
        self.caja_colision = pygame.Rect(offset_x, offset_y, tam_x, tam_y)
        self.velocidad = velocidad
    
    
        