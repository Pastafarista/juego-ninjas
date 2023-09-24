import pygame
from ajustes import *

def cargar_imagen(ruta):
    return pygame.image.load(ruta).convert_alpha()

def cargar_spritesheet_animacion_por_columnas(ruta_spritesheet):
    # Cargar la imagen
    imagen = cargar_imagen(ruta_spritesheet)
    
    # Crear lista de imagenes
    imagenes = []
    
    # Obtener dimensiones de la imagen
    ancho, alto = imagen.get_size()
    
    # Recorrer la imagen
    for x in range(0, ancho, 16):
        col = []
        for y in range(0, alto, 16):
            # Crear imagen
            cuadro = pygame.Surface((16, 16), pygame.SRCALPHA)
            cuadro.blit(imagen, (0, 0), (x, y, 16, 16))
            col.append(cuadro)
        imagenes.append(col)
            
    # Devolver lista de imagenes
    return imagenes

#Función que trocea una imagen en una lista de imagenes
def cargar_spritesheet(ruta_spritesheet):
    # Cargar la imagen
    imagen = cargar_imagen(ruta_spritesheet)
    
    # Crear lista de imagenes
    imagenes = []
    
    # Obtener dimensiones de la imagen
    ancho, alto = imagen.get_size()
    
    print("Ancho: " + str(ancho))
    print("Alto: " + str(alto))
    
    # Recorrer la imagen
    for fila in range(0, int(alto / TAM_TILE)):
        for columna in range(0, int(ancho / TAM_TILE)):
            
            x = columna * TAM_TILE
            y = fila * TAM_TILE
            
            # Crear imagen
            cuadro = pygame.Surface((16, 16), pygame.SRCALPHA)
            cuadro.blit(imagen, (0, 0), (x, y, 16, 16))
            imagenes.append(cuadro)
            
    # Devolver lista de imagenes
    print("Cargando spritesheet: " + ruta_spritesheet)
    print("Número de imagenes: " + str(len(imagenes)))
    return imagenes

def redimensionar_imagen(imagen, escala):
    return pygame.transform.scale(imagen, (int(imagen.get_width() * escala), int(imagen.get_height() * escala)))

def redimensionar_imagenes(imagenes, escala):
    imagenes_redimensionadas = []
    
    for imagen in imagenes:
        imagenes_redimensionadas.append(redimensionar_imagen(imagen, escala))
        
    return imagenes_redimensionadas