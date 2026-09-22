def busqueda_lineal(lista, objetivo):
    posicion = -1
    for i in range(0, len(lista)):
        if lista[i] == objetivo:
            posicion = i
    return posicion

def busqueda_binaria(lista, objetivo):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == objetivo:
            return medio
        if lista[medio] > objetivo:
            der = medio - 1
        else:
            izq = medio + 1
    return -1
    