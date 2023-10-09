from ajustes import *
from hud import Hud

class Camara():
    def __init__(self, jugador):
        self.x = 0
        self.y = 0
        self.limite_x = 0
        self.limite_y = 0
        self.x_final = 0
        self.y_final = 0
        
        self.jugador = jugador
        self.hud = Hud(jugador)
        
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
                imagen_x = (tile.columna * TAM_TILE - self.x) * ESCALA_ZOOM + self.offset_x
                imagen_y = (tile.fila * TAM_TILE - self.y) * ESCALA_ZOOM + self.offset_y
                
                if imagen_x + TAM_TILE * ESCALA_ZOOM >= 0 and imagen_x < LARGO_PANTALLA and imagen_y + TAM_TILE * ESCALA_ZOOM >= 0 and imagen_y < ALTO_PANTALLA:
                    imagenes_por_capas[capa].append((self.jugador.mapa.imagenes[tile.tipo],(imagen_x, imagen_y)))

        # Obtener las imagenes de las entidades del mapa donde está el jugador
        for entidad in self.jugador.mapa.entidades + self.jugador.mapa.enemigos:
            
            imagen_x = (entidad.pos_x - self.x) * ESCALA_ZOOM + self.offset_x
            imagen_y = (entidad.pos_y - self.y) * ESCALA_ZOOM + self.offset_y
            
            if imagen_x + TAM_TILE * ESCALA_ZOOM >= 0 and imagen_x < LARGO_PANTALLA and imagen_y + TAM_TILE * ESCALA_ZOOM >= 0 and imagen_y < ALTO_PANTALLA:
                imagenes_por_capas[entidad.sprite.capa].append((entidad.sprite.obtener_frame_actual(), (imagen_x, imagen_y)))
         
        # Obtener las imagenes de las armas del jugador   
        imagen_x = (self.jugador.arma.pos_x - self.x) * ESCALA_ZOOM + self.offset_x
        imagen_y = (self.jugador.arma.pos_y - self.y) * ESCALA_ZOOM + self.offset_y
        imagenes_por_capas[self.jugador.arma.sprite.capa].append((self.jugador.arma.sprite.obtener_frame_actual(), (imagen_x, imagen_y)))
            
        #ordenar las capas en función de imagen_y para que se rendericen en el orden adecuado
        for capa in range(numero_capas):
            imagenes_por_capas[capa].sort(key=lambda x: x[1][1])
            
        return imagenes_por_capas
    
    def render_imagen(self, pantalla, imagen, posicion):   
        pantalla.blit(imagen, posicion)
        
    def render(self, pantalla):      
        imagenes = self.obtener_imagenes_por_capas()
        
        for capa in imagenes:
            for imagen in capa:
                self.render_imagen(pantalla, imagen[0], imagen[1])
                
        #renderizar las imagenes del hud
        self.hud.render(pantalla)
    
    #Actualiza la posición de la cámara en función de la posición del jugador    
    def actualizar(self):
        x = self.jugador.pos_x
        y = self.jugador.pos_y
        
        offset_camara_x = LARGO_PANTALLA / (2 * ESCALA_ZOOM)
        offset_camara_y = ALTO_PANTALLA / (2 * ESCALA_ZOOM)
        
        #Si el jugador está fuera del mapa la cámara se para
        if x - offset_camara_x  >= 0 and x + offset_camara_x < self.jugador.mapa.largo:
            self.x = self.jugador.pos_x
        if y - offset_camara_y >= 0 and y + offset_camara_y < self.jugador.mapa.alto:
            self.y = self.jugador.pos_y
            
    