from ciudadano import Ciudadano

class Comunidad:
    def __init__(self, num_ciudadanos, enfermedad, num_infectados):
        self.enfermedad = enfermedad
        self.ciudadanos = self.crear_ciudadanos(num_ciudadanos, num_infectados)

    def crear_ciudadanos(self, num_ciudadanos, num_infectados):
        ciudadanos = [Ciudadano(id=i, comunidad=self) for i in range(num_ciudadanos)] #el rango lo llama desde el main

        #Infectar los primeros num_infectados ciudadanos de manera determinística
        for i in range(num_infectados):
            ciudadanos[i].estado = 'I'

        return ciudadanos
