# Lectura de la cadena de entrada
string = input()

# Separación y eliminación de espacios sobrantes
string_numbers = string.split(',')
numbers_list = list(map(lambda text: int(text.strip()), string_numbers))

print(f"List -> {numbers_list} / Tuple -> {tuple(numbers_list)}")