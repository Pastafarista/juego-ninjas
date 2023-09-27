import json
from tile import *
from ajustes import *
from teleport import Teleport
import herramientas_imagen as hi
import pygame

class Mapa:
    def __init__(self, ruta_archivo_mapa, mundo):
        self.nombre = ruta_archivo_mapa.split("/")[-1].split(".")[0]
        self.archivo = json.load(open(ruta_archivo_mapa))
        self.entidades = []
        self.imagenes = []
        self.mundo = mundo
        self.cargar()

    def cargar(self):
        self.tiles_alto = self.archivo["height"]
        self.tiles_largo = self.archivo["width"]
        
        self.largo = self.tiles_largo * TAM_TILE
        self.alto = self.tiles_alto * TAM_TILE
        
        self.obtener_nombre_tilesets()
        self.cargar_imagenes_tilesets()
        self.cargar_capas()
        self.cargar_colisiones()
        self.cargar_objetos()
     
    #Carga todas las capas del mapa a partir del archivo json   
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
                    if columna >= self.tiles_largo:
                        columna = 0
                        fila += 1
                
                indice_capa += 1
                
            
        self.numero_capas = indice_capa
     
    #Carga las colsiones del mapa a partir del archivo json
    def cargar_colisiones(self):
        self.hitboxes = []
        
        for capa in self.archivo["layers"]:
            
            if(capa.get("type") == "objectgroup" and capa.get("name") == "colisiones"):
                
                colisiones = capa["objects"]
                
                for colision in colisiones:
                    self.hitboxes.append(pygame.Rect(colision["x"], colision["y"], colision["width"], colision["height"]))
                 
    #Carga los objetos del mapa a partir del archivo json   
    def cargar_objetos(self):
        self.objetos = {"teleport": []}
        
        for capa in self.archivo["layers"]:
                
                if(capa.get("type") == "objectgroup" and capa.get("name") == "objetos"):
                    
                    objetos = capa["objects"]
                    
                    for objeto in objetos:
                        if objeto["class"] == "teleport":
                            
                            propiedades = objeto["properties"]
                            
                            for propiedad in propiedades:
                                if(propiedad["name"] == "mapa"):
                                    nombre_mapa_destino = propiedad["value"]
                                elif(propiedad["name"] == "posX"):
                                    destino_x = float(propiedad["value"])
                                elif(propiedad["name"] == "posY"):
                                    destino_y = float(propiedad["value"])
                            
                            self.objetos["teleport"].append(Teleport(objeto["x"], objeto["y"], objeto["width"], objeto["height"] , self.nombre, nombre_mapa_destino, destino_x, destino_y))
                
    #Obtiene los tilesets que se van a utilizar para el mapa en el orden adecuado, (el orden es importante porque los ids de las tiles va en función del orden en el que se cargan los tilesets)
    def obtener_nombre_tilesets(self):
        self.nombre_tilesets = []
        
        lista_blanca = open("tilesets.txt", "r").read().replace(" ", "").split("\n")
        
        for tileset_json in self.archivo["tilesets"]:    
            tileset = tileset_json["source"].split("/")[-1].split(".")[0] + ".png"
            
            if(tileset in lista_blanca):
                self.nombre_tilesets.append(tileset)
     
    #Cargar todas las imagenes de los tilesets y redimensionarlas                    
    def cargar_imagenes_tilesets(self):
        if len(self.nombre_tilesets) == 0:
            print("No hay tilesets")
            return
        
        for nombre_tileset in self.nombre_tilesets:
            self.imagenes += hi.cargar_spritesheet("res/Backgrounds/Tilesets/" + nombre_tileset)
            
        self.imagenes = hi.redimensionar_imagenes(self.imagenes, ESCALA_ZOOM)
        
    def actualizar(self):
        for entidad in self.entidades:
            entidad.actualizar()