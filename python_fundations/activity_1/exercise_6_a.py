def get_middle_substring(string, min_length, substring_length):
    if len(string) < min_length or len(string) < substring_length:
        return f"[ERROR] Input no valid, must be greater than {min_length} or {substring_length}"

    # Calcular número de caracteres en el margen izquierdo
    # En caso de cadenas de tamaño impar se selecciona el menor.
    margin = int((len(string) - substring_length) / 2)

    # Extraer la cadena desde la posición del margen calculado
    return string[margin: margin + substring_length]


print(get_middle_substring(input(), 7, 3))
