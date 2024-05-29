def quicksort(miLista):
    if len(miLista) <= 1:
        return miLista

    # Selección del pivote
    pivote = miLista[0]

    # Partición de la lista
    izquierda = []
    derecha = []
    medio = []

    for x in miLista:
        if x < pivote:
            izquierda.append(x)
        elif x > pivote:
            derecha.append(x)
        else:
            medio.append(x)

    # Llamadas recursivas y concatenación de resultados
    return quicksort(izquierda) + medio + quicksort(derecha)

# Función de prueba
def prueba_quicksort():
    prueba_list = [20,54,12,9,5,2,1,99,88]
    orden_list = quicksort(prueba_list)
    print("Lista original:", prueba_list)
    print("Lista ordenada:", orden_list)

# Ejecutar prueba e imprimir el resultado
prueba_quicksort()