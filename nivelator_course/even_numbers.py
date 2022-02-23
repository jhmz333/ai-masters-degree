#Inicializando la lista
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Filtrar los números pares de la lista e imprimirlos por pantalla
even_numbers = list(filter(lambda element: ( element % 2 == 0), my_list))
print(even_numbers)