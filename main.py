from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador

# Definición de la enfermedad con una probabilidad de recuperación diaria
covid = Enfermedad(infeccion_probable=0.3, recuperacion_probable=0.03)

# Definición de la comunidad
talca = Comunidad(num_ciudadanos=2000, enfermedad=covid, num_infectados=10)

# Inicialización del simulador
sim = Simulador()
sim.set_comunidad(talca)
sim.run(pasos=50)
