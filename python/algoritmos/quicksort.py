def quicksort(lista, primero, ultimo):
    copia = lista.copy()
    izquierda = primero
    derecha = ultimo - 1
    pivote = ultimo
    while izquierda < derecha:
        while copia[izquierda] < copia[pivote] and izquierda <= derecha:
            izquierda += 1
        while copia[derecha] > copia[pivote] and derecha >= izquierda:
            derecha -= 1
        if izquierda < derecha:
            copia[izquierda], copia[derecha] = copia[derecha], copia[izquierda]
    if copia[pivote] < copia[izquierda]:
        copia[izquierda], copia[pivote] = copia[pivote], copia[izquierda]
    if primero < izquierda:
        quicksort(copia, primero, izquierda - 1)
    if ultimo > izquierda:
        quicksort(copia, izquierda + 1, ultimo)
    return copia

