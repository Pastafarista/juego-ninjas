from mapa import *

class Mundo:
    def __init__(self):
        self.jugador = None
        self.mapas = {}
        self.cargar_mapas(["mapas/mundo.json", "mapas/casa01.json", "mapas/casa02.json", "mapas/forja01.json"])
        
    def cargar_mapas(self, rutas_mapas):
        for ruta_mapa in rutas_mapas:
            mapa = Mapa(ruta_mapa, self)
            self.mapas[mapa.nombre] = mapa
            print("Cargado mapa: " + mapa.nombre)
    
    def actualizar(self, dt):
        if(self.jugador):
            self.jugador.mapa.actualizar(dt)
    