class Animacion:
    def __init__(self, imagenes):
        self.imagenes = imagenes
        self.numero_frames = len(imagenes)
        self.frame_actual = 0
        self.tiempo = 0
        self.duracion_frame = 10
        
    def obtener_frame_actual(self):
        return self.imagenes[self.frame_actual] 
        
    def siguiente_frame(self, dt):
        self.tiempo += round(1 * dt * 60)
        
        if self.tiempo >= self.duracion_frame:
            self.tiempo = 0
            self.frame_actual += 1
            
            if self.frame_actual >= self.numero_frames:
                self.frame_actual = 0
        
    def reiniciar(self):
        self.frame_actual = 0
        
