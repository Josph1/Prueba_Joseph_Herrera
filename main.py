def encontrar_el_subarreglo(arreglo_inicial, numero_objetivo):
    n = len(arreglo_inicial)
    max_tamaño = 0
    arreglo_maximo = []

    for i in range(n):
        suma_actual = 0
        for j in range(i, n):
            suma_actual += arreglo_inicial[j]
            if suma_actual == numero_objetivo and (j - i + 1) > max_tamaño:
                max_tamaño = j - i + 1
                arreglo_maximo = arreglo_inicial[i:j+1]

    if max_tamaño == 0:
        return None  # No subarray found with the target sum
    return arreglo_maximo

        
    
