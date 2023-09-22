import pygame

def cargar_imagen(ruta):
    return pygame.image.load(ruta).convert_alpha()

def cargar_imagenes(ruta_spritesheet):
    # Cargar la imagen
    imagen = cargar_imagen(ruta_spritesheet)
    
    # Crear lista de imagenes
    imagenes = []
    
    # Obtener dimensiones de la imagen
    ancho, alto = imagen.get_size()
    
    # Recorrer la imagen
    for x in range(0, ancho, 32):
        for y in range(0, alto, 32):
            # Crear imagen
            cuadro = pygame.Surface((32, 32), pygame.SRCALPHA)
            cuadro.blit(imagen, (0, 0), (x, y, 32, 32))
            imagenes.append(cuadro)
            
    # Devolver lista de imagenes
    return imagenes

