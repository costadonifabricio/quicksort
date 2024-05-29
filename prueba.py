from main import quicksort

# Función de prueba
def prueba_quicksort():
    prueba_list = [20,54,12,9,5,2,1,99,88]
    orden_list = quicksort(prueba_list)
    print("Lista original:", prueba_list)
    print("Lista ordenada:", orden_list)

# Ejecutar prueba e imprimir el resultado
prueba_quicksort()