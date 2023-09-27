import time

class Timer():
    def __init__(self, tiempo):
        self.tiempo = tiempo
        self.tiempo_inicio = 0
        self.activado = False
        
    def __init__(self):
        self.tiempo = 0
        self.tiempo_inicio = 0
        self.activado = False
        
    def activar(self):
        self.activado = True
        self.tiempo_actual = time.perf_counter()
        
    def activar(self, tiempo):
        self.tiempo = tiempo
        self.activado = True
        self.tiempo_actual = time.perf_counter()
        
    def actualizar(self):
        if self.activado:
            if time.perf_counter() - self.tiempo_actual >= self.tiempo:
                self.activado = False
                return True
            
    