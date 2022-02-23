import tensorflow as tf

list_1 = tf.constant([1, 4, 5, 6])
list_2 = tf.constant([3, 6, 7, 3])

# Multiplicación de 2 listas usando el método tf.math.multiply
# result = tf.math.multiply(list_1, list_2)

# Multiplicación de 2 listas usando el operador *
result = list_1 * list_2

# Imprimiendo la lista resultado
print(result)