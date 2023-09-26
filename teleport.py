import pygame

class Teleport():
    def __init__(self, x, y, tamX, tamY, origen, destino, x_destino, y_destino):
        self.x = x;
        self.y = y;
        
        self.tamX = tamX;
        self.tamY = tamY;
        
        self.origen = origen;
        self.destino = destino;
        
        self.x_destino = x_destino;
        self.y_destino = y_destino;
        
        