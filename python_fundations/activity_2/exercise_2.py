# SyntaxError: Excepción que se produce cuando se ha escrito erroneamente una instrucción.
text = 'Texto que no cierra

# ZeroDivisionError: Excepción que ocurre cuando no tengo se intenta hacer una división con denominador igual a cero.
result = 10 / 0

# FileNotFoundError: Excepción que se produce cuando se intenta abrir un fichero que no existe, o no puedo leer.
file_no_exist = open('file_not_found.txt')

# IndexError: Excepción que ocurre cuando se intenta acceder a una posición de una lista que no existe
number_list = [1, 2, 3, 4, 5]
six = number_list[5]

# KeyError: Excepción que se lanza cuando se intenta acceder a una clave no existente de un diccionario.
dictionary = {
    'key1': 'value1',
    'key2': 'value2'
}
value3 = dictionary['key3']