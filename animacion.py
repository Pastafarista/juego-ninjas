class Animacion:
    def __init__(self, imagenes):
        self.imagenes = imagenes
        self.numero_frames = len(imagenes)
        self.frame_actual = 0
        
    def obtener_frame_actual(self):
        return self.imagenes[self.frame_actual] 
        
    def siguiente_frame(self):
        self.frame_actual = (self.frame_actual + 1) % self.numero_frames
        
    def reiniciar(self):
        self.frame_actual = 0
        
