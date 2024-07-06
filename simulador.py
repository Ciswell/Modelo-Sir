class Simulador:
    def __init__(self): #listas de los estados de los ciudadanos
        self.susceptibles = []
        self.infectados = []
        self.recuperados = []

    def set_comunidad(self, comunidad): #clasifica a los ciudadanos segun su estado
        self.comunidad = comunidad
        self.susceptibles = [c for c in comunidad.ciudadanos if c.estado == 'S']
        self.infectados = [c for c in comunidad.ciudadanos if c.estado == 'I']
        self.recuperados = [c for c in comunidad.ciudadanos if c.estado == 'R']

    def run(self, pasos):
        for dia in range(pasos):
            self.simular_paso()
            print(
                f"Dia {dia + 1}: Susceptibles: {len(self.susceptibles)}, Infectados: {len(self.infectados)}, Recuperados: {len(self.recuperados)}")

    def simular_paso(self):
        nuevos_infectados = []
        nuevos_recuperados = []

        #Calcular número de nuevos infectados determinísticamente
        tasa_infeccion = self.comunidad.enfermedad.infeccion_probable # tasa_infeccion es la probabilidad de infección lo llama desde el main
        nuevos_infectados_count = int( #calcula el número de nuevos infectados con la tasa de infección y la interacción entre infectados y susceptibles
            tasa_infeccion * len(self.infectados) * len(self.susceptibles) / len(self.comunidad.ciudadanos)) # Representa el potencial de interacción entre los infectados y los susceptibles

        #Limitar el número de nuevos infectados al número de susceptibles
        nuevos_infectados_count = min(nuevos_infectados_count, len(self.susceptibles)) #Esta línea asegura que el numero de nuevos infectados no supere a los susceptibles disponibles

        for i in range(nuevos_infectados_count): #se utiliza para añadir los ciudadanos que se han infectado (inter desde 0 hasta nuevo infectado)
            nuevos_infectados.append(self.susceptibles[i]) #busca en la lista de suceptibles para infectarlos

        #Calcular número de nuevos recuperados determinísticamente
        tasa_recuperacion = self.comunidad.enfermedad.recuperacion_probable #es la probabilidad diaria de que un ciudadano infectado se recupere.
        nuevos_recuperados_count = int(tasa_recuperacion * len(self.infectados))

        #Limitar el número de nuevos recuperados al número de infectados
        nuevos_recuperados_count = min(nuevos_recuperados_count, len(self.infectados))

        for i in range(nuevos_recuperados_count): #busca en la lista de nuevos_recuperados
            nuevos_recuperados.append(self.infectados[i]) #busca en la lista de infectados para que se recuperen

        #actualiza el estado remueve de la lista susceptibles a la lista de infectados
        for infectado in nuevos_infectados:
            self.susceptibles.remove(infectado) #remueve al ciudadano de la lista de S
            infectado.estado = 'I' #Cambia su estado
            infectado.pasos_infectado = 0 #resetea su contador
            self.infectados.append(infectado) #añade el ciudadano a la lista de infectados

        for recuperado in nuevos_recuperados:
            self.infectados.remove(recuperado)
            recuperado.estado = 'R'
            self.recuperados.append(recuperado)