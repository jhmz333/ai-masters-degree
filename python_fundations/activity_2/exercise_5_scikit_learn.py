# Importando los datasets por defecto diabetes y digits
from sklearn.datasets import load_diabetes
from sklearn.datasets import load_digits

# Imprimiendo los datos del dataset digits
print(load_digits().data)