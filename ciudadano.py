class Ciudadano:
    def __init__(self, id, comunidad, estado='S'):
        self.id = id
        self.comunidad = comunidad
        self.estado = estado  #'S' para susceptible, 'I' para infectado, 'R' para recuperado
        self.pasos_infectado = 0
