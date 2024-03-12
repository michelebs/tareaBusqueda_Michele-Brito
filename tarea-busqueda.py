# Búsqueda lineal de forma recursiva
def busqueda_lineal_recursiva(lista, elemento, indice=0):
    if indice >= len(lista):
        return -1
    if lista[indice] == elemento:
        return indice
    return busqueda_lineal_recursiva(lista, elemento, indice + 1)

# Búsqueda binaria de forma iterativa
def busqueda_binaria_iterativa(lista, elemento):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

# Ejemplo de uso
mi_lista = [1, 3, 5, 7, 9, 11, 13, 15]
elemento_busqueda = 7

# Búsqueda lineal recursiva
resultado_lineal = busqueda_lineal_recursiva(mi_lista, elemento_busqueda)
print(f"Resultado búsqueda lineal recursiva: {resultado_lineal}")

# Búsqueda binaria iterativa
mi_lista.sort()  # Asegurarse de que la lista esté ordenada para la búsqueda binaria
resultado_binario = busqueda_binaria_iterativa(mi_lista, elemento_busqueda)
print(f"Resultado búsqueda binaria iterativa: {resultado_binario}")
