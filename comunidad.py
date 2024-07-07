from ciudadano import Ciudadano
import random

class Comunidad:
    def __init__(self, num_ciudadanos, enfermedad, num_infectados):
        self.enfermedad = enfermedad
        self.ciudadanos = self.crear_ciudadanos(num_ciudadanos, num_infectados)

    def crear_ciudadanos(self, num_ciudadanos, num_infectados):
        ciudadanos = [Ciudadano(id=i, comunidad=self) for i in range(num_ciudadanos)]

        # Infectar los primeros num_infectados ciudadanos
        infectados_iniciales = random.sample(ciudadanos, num_infectados)
        for infectado in infectados_iniciales:
            infectado.estado = 'I'

        return ciudadanos

    def actualizar_contactos(self):
        for ciudadano in self.ciudadanos:
            ciudadano.contactos = []
            num_contactos = random.randint(0, 8)  #Permitir entre 0 y 8 contactos
            contactos = random.sample(self.ciudadanos, k=num_contactos)
            for contacto in contactos:
                if contacto != ciudadano:
                    ciudadano.agregar_contacto(contacto)
                    contacto.agregar_contacto(ciudadano)
