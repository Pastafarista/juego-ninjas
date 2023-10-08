from mapa import *

class Mundo:
    def __init__(self):
        self.mapas = {}
        self.cargar_mapas(["mapas/mundo.json", "mapas/casa01.json", "mapas/casa02.json", "mapas/forja01.json"])
        
    def cargar_mapas(self, rutas_mapas):
        for ruta_mapa in rutas_mapas:
            mapa = Mapa(ruta_mapa, self)
            self.mapas[mapa.nombre] = mapa
            print("Cargado mapa: " + mapa.nombre)
    
    def actualizar(self, dt):
        self.actualizar_mapas(dt)
    
    def actualizar_mapas(self, dt):
        for mapa in self.mapas.values():
            mapa.actualizar(dt)
    