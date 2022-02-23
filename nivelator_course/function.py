# Función que resta dos números y muestra error si el resultado es negativo
def subtraction(number1, number2, show_message=False):
    result = number1 - number2
    error_message = ""
    if (show_message and result < 0):
        error_message = "¡Error!, el resultado es negativo"
    return (result, error_message)

# Llamado de la función con varios parámetros
print("El resultado de la resta es: %f %s" % subtraction(15, 12))
print("El resultado de la resta es: %f %s" % subtraction(15, 12, True))
print("El resultado de la resta es: %f %s" % subtraction(12, 15))
print("El resultado de la resta es: %f %s" % subtraction(12, 15, True))