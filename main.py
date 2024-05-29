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

