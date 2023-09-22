import json
from tile import *

class Mapa:
    def __init__(self, ruta_archivo_mapa):
        self.archivo = json.load(open(ruta_archivo_mapa))
        self.entidades = []
        self.imagenes = {}
        self.cargar()

    def cargar(self):
        self.alto = self.archivo["height"]
        self.largo = self.archivo["width"]
        
        self.cargarTilesets()
        self.cargarCapas()
        
    def cargarCapas(self):
        self.tiles = []
        
        indice_capa = 0
        
        for capa in self.archivo["layers"]:
            
            if(capa.get("type") == "tilelayer"):
            
                data = capa["data"]
                
                fila = 0
                columna = 0
                
                for numero in data:
                    if numero != 0:
                        self.tiles.append(Tile(fila, columna, numero, capa))
                        
                    columna += 1 
                    if fila >= self.largo - 1:
                        columna = 0
                        fila += 1
                
                indice_capa += 1
            
        self.numero_capas = capa
                
    def cargarTilesets(self):
        self.tilesets = []
        
        lista_blanca = open("tilesets.txt", "r").read().replace(" ", "").split("\n")
        
        for tileset_json in self.archivo["tilesets"]:    
            tileset = tileset_json["source"].split("/")[-1].split(".")[0] + ".png"
            
            if(tileset in lista_blanca):
                self.tilesets.append(tileset)

            
    