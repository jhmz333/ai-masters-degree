try:
    # Abre el archivo en modo lectura
    file = open("data.csv", "r")

    #Imprime por pantalla cada línea del archivo
    print(file.read())
except Exception as e:
    # Se captura excepción para controlar el mensaje del error
    print("Problemas al abrir el archivo data.csv: " + e.__str__())