import numpy as np 
import pygame
from timer import Timer
import math

class Entidad:
    def __init__(self, pos_x, pos_y, offset_x, offset_y, tam_x, tam_y, velocidad, mapa):
        
        # Posición en píxeles (están truncadas a enteros)
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        # Posición real (con decimales)
        self.pos_x_real = pos_x
        self.pos_y_real = pos_y
        
        self.caja_colision = pygame.Rect(pos_x, pos_y, tam_x, tam_y)
        self.velocidad = velocidad
        self.direccion = np.array([0, 0], dtype=float)
        self.tam_x = tam_x
        self.tam_y = tam_y
        self.mapa = mapa
        
        self.offset_x = offset_x
        self.offset_y = offset_y
        
        self.timers = {}
        self.añadir_timer("desplazarse")
    
    #Moverse en la dirección actual en un frame
    def moverse(self, dt):  
        #Normalizar la dirección para que no vaya más rápido en diagonal
        if(self.direccion[0] != 0 and self.direccion[1] != 0):
            self.direccion = self.direccion / np.sqrt(np.sum(self.direccion**2))
            
        dx = self.velocidad * self.direccion[0] * dt
        dy = self.velocidad * self.direccion[1] * dt
        
        #Ver si el movimiento va a colisionar con alguna hitbox del mapa o con los límites del mapa
        
        #Primero en x
        hitbox_temporal = self.caja_colision.copy().move(round(dx) + round(self.direccion[0]), 0)
        
        for hitbox in self.mapa.hitboxes:
            if hitbox_temporal.colliderect(hitbox) or hitbox_temporal.x < 0 or hitbox_temporal.x + hitbox_temporal.width > self.mapa.largo:
                dx = 0
        
        #Luego en y 
        hitbox_temporal = self.caja_colision.copy().move(0 , round(dy) + round(self.direccion[1]))
        
        for hitbox in self.mapa.hitboxes:
            if hitbox_temporal.colliderect(hitbox) or hitbox_temporal.y < 0 or hitbox_temporal.y + hitbox_temporal.height > self.mapa.alto:
                dy = 0
        
        # Actualizar la posición real
        self.pos_x_real += dx
        self.pos_y_real += dy
        
        # Actualizar la posición truncada
        self.pos_x = int(self.pos_x_real)
        self.pos_y = int(self.pos_y_real)
        
        #Actualizar la caja de colisiones
        self.actualizar_hitbox()
    
    #Desplazarse en una dirección durante un tiempo
    def desplazarse(self, direccion, tiempo):
        self.direccion = direccion
        self.timers["desplazarse"].activar(tiempo)
       
    #Ver si se está desplazando 
    def se_esta_desplazando(self):
        return self.timers["desplazarse"].activado
    
    def actualizar_timers(self):
        for timer in self.timers.values():
            timer.actualizar()
        
    def añadir_timer(self, nombre):
        self.timers[nombre] = Timer()
        
    def actualizar_hitbox(self):
        self.caja_colision.x = self.pos_x + self.offset_x
        self.caja_colision.y = self.pos_y + self.offset_y
                
    def actualizar(self, dt):
        self.moverse(dt)
        self.actualizar_timers()