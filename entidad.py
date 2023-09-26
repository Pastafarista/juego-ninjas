import numpy as np 
import pygame

class Entidad:
    def __init__(self, pos_x, pos_y, offset_x, offset_y, tam_x, tam_y, velocidad, mapa):
        self.posicion = np.array([pos_x, pos_y], dtype=float)
        self.caja_colision = pygame.Rect(pos_x, pos_y, tam_x, tam_y)
        self.velocidad = velocidad
        self.direccion = np.array([0, 0], dtype=float)
        self.tam_x = tam_x
        self.tam_y = tam_y
        self.mapa = mapa
    
    def moverse(self):  
        #Normalizar la dirección para que no vaya más rápido en diagonal
        if(self.direccion[0] != 0 and self.direccion[1] != 0):
            self.direccion = self.direccion / np.sqrt(np.sum(self.direccion**2))
            
            
        dx = self.direccion[0] * self.velocidad
        dy = self.direccion[1] * self.velocidad
        
        #Comprobar colisiones con el mapa
        for hitbox in self.mapa.hitboxes:
            if self.caja_colision.move(dx, 0).colliderect(hitbox):
                dx = 0
            if self.caja_colision.move(0, dy).colliderect(hitbox):
                dy = 0
            
        self.posicion += np.array([dx, dy])
        
        #Actualizar la caja de colisiones
        self.caja_colision.x = self.posicion[0] 
        self.caja_colision.y = self.posicion[1]
        
    def comprobar_colisiones(self):
        #Comprobar colisiones con el mapa
        for hitbox in self.mapa.hitboxes:
            if self.caja_colision.colliderect(hitbox):
                print("Colisión")
                
    def actualizar(self):
        self.comprobar_colisiones()
        self.moverse()