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
                imagen_x = tile.columna * TAM_TILE
                imagen_y = tile.fila * TAM_TILE
                
                imagenes_por_capas[capa].append((self.jugador.mapa.imagenes[tile.tipo],(imagen_x, imagen_y)))

        for entidad in self.jugador.mapa.entidades + self.jugador.mapa.enemigos:
            imagenes_por_capas[entidad.capa].append((entidad.obtener_frame_actual(), (entidad.pos_x, entidad.pos_y)))
            
        #ordenar las capas en función de imagen_y para que se rendericen en el orden adecuado
        for capa in range(numero_capas):
            imagenes_por_capas[capa].sort(key=lambda x: x[1][1])
            
        return imagenes_por_capas
    
    def render_imagen(self, pantalla, imagen, posicion):   
        imagen_x = posicion[0]
        imagen_y = posicion[1]
        
        #Si la imagen está fuera de la pantalla no se renderiza
        if imagen_x < self.x or imagen_x > self.x_final or imagen_y < self.y or imagen_y > self.y_final:
            pantalla.blit(imagen, ( (posicion[0] - self.x) * ESCALA_ZOOM + self.offset_x, (posicion[1] - self.y) * ESCALA_ZOOM + self.offset_y) )
        
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
            
    