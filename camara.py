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
        
    def render_mapa(self, pantalla):
        for capa in range(self.jugador.mapa.numero_capas):
            for tile in self.jugador.mapa.tiles_por_capas[capa]:
                self.render_tile(tile, pantalla)
        
    def render_tile(self, tile, pantalla):     
        imagen_x = tile.columna * TAM_TILE
        imagen_y = tile.fila * TAM_TILE
        
        pantalla.blit(self.jugador.mapa.imagenes[tile.tipo], ( (imagen_x - self.x) * ESCALA_ZOOM + self.offset_x, (imagen_y - self.y) * ESCALA_ZOOM + self.offset_y) )
        
    def render_entidad(self, entidad_con_sprite, pantalla):
        pantalla.blit(entidad_con_sprite.obtener_frame_actual(), ( (entidad_con_sprite.posicion[0] - self.x) * ESCALA_ZOOM + self.offset_x, (entidad_con_sprite.posicion[1] - self.y) * ESCALA_ZOOM + self.offset_y) )
        
    def actualizar(self):
        jugador_pos_x = self.jugador.posicion[0]
        jugador_pos_y = self.jugador.posicion[1]

        self.x = jugador_pos_x
        self.y = jugador_pos_y
    