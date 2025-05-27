def calcular_promedio(lista_numeros):
    """
    Calcula el promedio de una lista de números.
    Parámetros:
    lista_numeros (list): Lista de números (int o float)
    Retorna:
    float: Promedio de los números en la lista
    """
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

# Ejemplo de uso con una lista larga:
numeros = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
print("Promedio:", calcular_promedio(numeros))  # El promedio será 66.0