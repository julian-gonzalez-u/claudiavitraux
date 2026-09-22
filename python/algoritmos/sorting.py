def bubble_sort(lista):
    copia = lista.copy()
    i = 0
    control = True
    while i <= len(copia) - 2 and control:
        control = False
        for j in range(0, len(copia) - i - 1):
            if copia[j][1] > copia[j + 1][1]:
                copia[j][1], copia[j + 1][1] = copia[j + 1][1], copia[j][1]
                control = True
        i += 1
    return copia

def selection_sort(lista):
    copia = lista.copy()
    for i in range(0, len(copia) - 1):
        minimo = i
        for j in range(i + 1, len(copia)):
            if copia[j][1] < copia[minimo][1]:
                minimo = j
        copia[i][1], copia[minimo][1] = copia[minimo][1], copia[i][1]
    return copia

def insertion_sort(lista):
    copia = lista.copy()
    for i in range(1, len(copia) + 1):
        k = i - 1
        while k > 0 and copia[k][1] < copia[k - 1][1]:
            copia[k][1], copia[k - 1][1] = copia[k - 1][1], copia[k][1]
            k -= 1
    return copia

def mergesort(lista):
    copia = lista.copy()
    if len(copia) <= 1:
        return copia
    else:
        medio = len(copia) // 2
        izquierda = []
        for i in range(0, medio):
            izquierda.append(copia[i])
        derecha = []
        for i in range(medio, len(copia)):
            derecha.append(copia[i])
        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)
        if izquierda[medio - 1][1] <= derecha[0][1]:
            izquierda += derecha
            return izquierda
        resultado = merge(izquierda, derecha)
        return resultado

def merge(izquierda, derecha):
    lista_mezclada = []
    while len(izquierda) > 0 and len(derecha) > 0:
        if izquierda[0][1] < derecha[0][1]:
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    if len(izquierda) > 0:
        lista_mezclada += izquierda
    if len(derecha) > 0:
        lista_mezclada += derecha
    return lista_mezclada

def quicksort(lista, primero, ultimo):
    copia = lista.copy()
    izquierda = primero
    derecha = ultimo - 1
    pivote = ultimo
    while izquierda < derecha:
        while copia[izquierda][1] < copia[pivote][1] and izquierda <= derecha:
            izquierda += 1
        while copia[derecha][1] > copia[pivote][1] and derecha >= izquierda:
            derecha -= 1
        if izquierda < derecha:
            copia[izquierda][1], copia[derecha][1] = copia[derecha][1], copia[izquierda][1]
    if copia[pivote][1] < copia[izquierda][1]:
        copia[izquierda][1], copia[pivote][1] = copia[pivote][1], copia[izquierda][1]
    if primero < izquierda:
        quicksort(copia, primero, izquierda - 1)
    if ultimo > izquierda:
        quicksort(copia, izquierda + 1, ultimo)
    return copia

