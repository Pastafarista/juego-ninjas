import os
from PIL import Image
import json
import filetype

class Archivo:
    
    archivos = []
    
    def __init__(self, ruta, id):
        self.ruta = ruta
        self.id = id
        
    def actualizarArchivos():
        contador = 0

        for currentpath, folders, files in os.walk('./res'):
            for file in files:      
                ruta = os.path.join(currentpath, file).replace("\\", "/")
                
                if(filetype.is_image(ruta)):
                    img = Image.open(ruta)
                
                    largo = img.width
                    alto = img.height
                
                    archivo_imagen = ArchivoImagen(ruta, contador, largo, alto)
                    
                    Archivo.archivos.append(archivo_imagen)
                
                contador += 1
    
    def exportarArchivos():
                    
        lista_temporal = []
            
        f = open("res.txt", "w")

        for archivo in Archivo.archivos:
            lista_temporal.append(archivo.toDict())
                
        f.write(json.dumps(lista_temporal))



class ArchivoImagen(Archivo):
    def __init__(self, ruta, id, largo, alto):
        super().__init__(ruta, id)
        self.largo = largo
        self.alto = alto
        
    def toDict(self):
        dict = {"tipo":"imagen","ruta":self.ruta,"id":self.id,"largo":self.largo,"alto":self.alto}
        return dict


Archivo.actualizarArchivos()
Archivo.exportarArchivos()