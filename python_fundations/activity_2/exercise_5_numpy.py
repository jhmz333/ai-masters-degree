import numpy as np

# Mostrar versión y configuración
print(f"Versión: {np.__version__}")
print(f"\nConfiguración:")
np.__config__.show()

# Crear array de Numpy
array = np.array([[3, 3, 3, 3],
                  [3, 3, 3, 3],
                  [3, 3, 0, 3],
                  [3, 3, 3, 3]])

# Comprobar si el array tiene un cero
response = "" if not(array.all()) else "no "
print(f"\nEl arreglo de numpy {response}contiene el número cero")