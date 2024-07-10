import random

class Simulador:
    def __init__(self):
        self.susceptibles = []
        self.infectados = []
        self.recuperados = []
        self.umbral_infeccion = 1  # Umbral de interacciones necesarias para infectar

    def set_comunidad(self, comunidad):
        self.comunidad = comunidad
        self.susceptibles = [c for c in comunidad.ciudadanos if c.estado == 'S']
        self.infectados = [c for c in comunidad.ciudadanos if c.estado == 'I']
        self.recuperados = [c for c in comunidad.ciudadanos if c.estado == 'R']

    def run(self, pasos):
        for dia in range(pasos):
            self.comunidad.actualizar_contactos_diarios()  # Actualizar los contactos diarios
            self.simular_paso()
            print(f"Dia {dia + 1}: Susceptibles: {len(self.susceptibles)}, Infectados: {len(self.infectados)}, Recuperados: {len(self.recuperados)}")

    def simular_paso(self):
        nuevos_infectados = []
        nuevos_recuperados = []

        # Calcular número de nuevos infectados basado en contactos directos
        tasa_infeccion = self.comunidad.enfermedad.infeccion_probable * 0.5  # Ajustar la tasa de infección
        for infectado in self.infectados:
            for contacto in infectado.contactos_diarios:
                if contacto.estado == 'S':
                    # Contar interacciones con infectados
                    interacciones_infectados = sum(1 for i in contacto.contactos_diarios if i.estado == 'I')
                    if interacciones_infectados >= self.umbral_infeccion and random.random() < tasa_infeccion:
                        nuevos_infectados.append(contacto)

        # Calcular número de nuevos recuperados
        tasa_recuperacion = self.comunidad.enfermedad.recuperacion_probable
        for infectado in self.infectados:
            infectado.pasos_infectado += 1
            if infectado.pasos_infectado >= 15 or random.random() < tasa_recuperacion:
                nuevos_recuperados.append(infectado)

        # Actualización de estados
        for infectado in nuevos_infectados:
            if infectado in self.susceptibles:
                self.susceptibles.remove(infectado)
                infectado.estado = 'I'
                infectado.pasos_infectado = 0
                self.infectados.append(infectado)

        for recuperado in nuevos_recuperados:
            self.infectados.remove(recuperado)
            recuperado.estado = 'R'
            self.recuperados.append(recuperado)
