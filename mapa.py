import json
from tile import *
from ajustes import *
import herramientas_imagen as hi

class Mapa:
    def __init__(self, ruta_archivo_mapa):
        self.archivo = json.load(open(ruta_archivo_mapa))
        self.entidades = []
        self.imagenes = []
        self.cargar()

    def cargar(self):
        self.alto = self.archivo["height"]
        self.largo = self.archivo["width"]
        
        self.obtener_nombre_tilesets()
        self.cargar_imagenes_tilesets()
        self.cargar_capas()
        
    def cargar_capas(self):
        self.tiles_por_capas = []
        
        indice_capa = 0
        
        for capa in self.archivo["layers"]:
            
            self.tiles_por_capas.append([])
            
            if(capa.get("type") == "tilelayer"):
                
                data = capa["data"]
                fila = 0
                columna = 0
                
                for tipo in data:
                    if tipo != 0:
                        self.tiles_por_capas[indice_capa].append(Tile(fila, columna, tipo - 1, capa))
                        
                    columna += 1 
                    if columna >= self.largo:
                        columna = 0
                        fila += 1
                
                indice_capa += 1
                
            
        self.numero_capas = indice_capa
                
    def obtener_nombre_tilesets(self):
        self.nombre_tilesets = []
        
        lista_blanca = open("tilesets.txt", "r").read().replace(" ", "").split("\n")
        
        for tileset_json in self.archivo["tilesets"]:    
            tileset = tileset_json["source"].split("/")[-1].split(".")[0] + ".png"
            
            if(tileset in lista_blanca):
                self.nombre_tilesets.append(tileset)
                         
    def cargar_imagenes_tilesets(self):
        if len(self.nombre_tilesets) == 0:
            print("No hay tilesets")
            return
        
        for nombre_tileset in self.nombre_tilesets:
            self.imagenes += hi.cargar_spritesheet("res/Backgrounds/Tilesets/" + nombre_tileset)
            
        self.imagenes = hi.redimensionar_imagenes(self.imagenes, ESCALA_ZOOM)
        
        print(len(self.imagenes))
                        