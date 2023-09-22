import pygame

#Clase que gestiona los inputs del usuario
class Controles:
    def __init__(self):
        self.teclas = {"w":False,"a":False,"d":False,"s":False,"f":False,"r":False,"g":False}
        self.raton = {"izquierdo":False,"derecho":False, "medio":False}
        
    def actualizar_teclas(self):
        key = pygame.key.get_pressed()
        if (key[pygame.K_w] or key[pygame.K_UP]):
            self.teclas["w"] = True
        else:
            self.teclas["w"] = False
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.teclas["a"] = True
        else:
            self.teclas["a"] = False
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.teclas["d"] = True
        else:
            self.teclas["d"] = False
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.teclas["s"] = True
        else:
            self.teclas["s"] = False
        if key[pygame.K_f]:
            self.teclas["f"] = True
        else:
            self.teclas["f"] = False
        if key[pygame.K_r]:
            self.teclas["r"] = True
        else:
            self.teclas["r"] = False
        if key[pygame.K_g]:
            self.teclas["g"] = True
        else:
            self.teclas["g"] = False
            
    def actualizar_raton(self):
        izquierdo,medio,derecho = pygame.mouse.get_pressed()
        
        self.raton["izquierdo"] = izquierdo
        self.raton["medio"] = medio
        self.raton["derecho"] = derecho
        
    def actualizar(self):
        self.actualizar_teclas()
        self.actualizar_raton()
        
    def obtener_tecla(self,tecla):
        return self.teclas[tecla]
    
    def obtener_raton(self,boton):
        return self.raton[boton]
 