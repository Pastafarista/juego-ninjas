from ajustes import *

class Camara():
    def __init__(self, jugador):
        self.x = 0
        self.y = 0
        self.limite_x = 0
        self.limite_y = 0
        self.x_final = 0
        self.y_final = 0
        
        self.jugador = jugador
        
        self.offset_x = LARGO_PANTALLA / 2 - jugador.tam_x / 2
        self.offset_y = ALTO_PANTALLA / 2  - jugador.tam_y / 2
        
        self.camara_libre = True
    
    #Obtiene las imágenes de los tiles y entidades que se encuentran en la pantalla	para su posterior renderizado
    def obtener_imagenes_por_capas(self):
        imagenes_por_capas = []
        
        numero_capas = self.jugador.mapa.numero_capas
    
        for capa in range(numero_capas):
            imagenes_por_capas.append([])
            for tile in self.jugador.mapa.tiles_por_capas[capa]:
                imagen_x = tile.columna * TAM_TILE
                imagen_y = tile.fila * TAM_TILE
                
                imagenes_por_capas[capa].append((self.jugador.mapa.imagenes[tile.tipo],(imagen_x, imagen_y)))

        for entidad in self.jugador.mapa.entidades:
            imagenes_por_capas[entidad.capa].append((entidad.obtener_frame_actual(), (entidad.posicion[0], entidad.posicion[1])))
            
        return imagenes_por_capas
    
    def render_imagen(self, pantalla, imagen, posicion):
        pantalla.blit(imagen, ( (posicion[0] - self.x) * ESCALA_ZOOM + self.offset_x, (posicion[1] - self.y) * ESCALA_ZOOM + self.offset_y) )
        
    def render(self, pantalla):      
        imagenes = self.obtener_imagenes_por_capas()
        
        for capa in imagenes:
            for imagen in capa:
                self.render_imagen(pantalla, imagen[0], imagen[1])
    
    #Actualiza la posición de la cámara en función de la posición del jugador    
    def actualizar(self):
        jugador_pos_x = self.jugador.posicion[0]
        jugador_pos_y = self.jugador.posicion[1]

        self.x = jugador_pos_x
        self.y = jugador_pos_y
    