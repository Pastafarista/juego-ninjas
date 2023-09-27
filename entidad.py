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
        
        self.offset_x = offset_x
        self.offset_y = offset_y
    
    def moverse(self):  
        #Normalizar la dirección para que no vaya más rápido en diagonal
        if(self.direccion[0] != 0 and self.direccion[1] != 0):
            self.direccion = self.direccion / np.sqrt(np.sum(self.direccion**2))
            
            
        dx = self.direccion[0] * self.velocidad
        dy = self.direccion[1] * self.velocidad
        
        
        #Ver si el movimiento va a colisionar con alguna hitbox del mapa o con los límites del mapa
        
        #Primero en x
        hitbox_temporal = self.caja_colision.copy().move(dx, 0)
        
        for hitbox in self.mapa.hitboxes:
            if hitbox_temporal.colliderect(hitbox) or hitbox_temporal.x < 0 or hitbox_temporal.x + hitbox_temporal.width > self.mapa.largo:
                dx = 0
        
        #Luego en y 
        hitbox_temporal = self.caja_colision.copy().move(0, dy)
        
        for hitbox in self.mapa.hitboxes:
            if hitbox_temporal.colliderect(hitbox) or hitbox_temporal.y < 0 or hitbox_temporal.y + hitbox_temporal.height > self.mapa.alto:
                dy = 0
            
        self.posicion += np.array([round(dx), round(dy)])
        
        #Actualizar la caja de colisiones
        self.actualizar_hitbox()
        
    def actualizar_hitbox(self):
        self.caja_colision.x = self.posicion[0] + self.offset_x
        self.caja_colision.y = self.posicion[1] + self.offset_y
     
                
    def actualizar(self):
        self.moverse()