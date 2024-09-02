def encontrar_el_subarreglo(arreglo_inicial, numero_objetivo):
    n = len(arreglo_inicial)
    max_tamaño = 0
    arreglo_maximo = []

    #Itera sobre todos los posibles subarreglos, calculando su suma y comparándola con el objetivo
    for i in range(n):
        suma_actual = 0
        for j in range(i, n):
            suma_actual += arreglo_inicial[j]
            if suma_actual == numero_objetivo and (j - i + 1) > max_tamaño:
                max_tamaño = j - i + 1
                arreglo_maximo = arreglo_inicial[i:j+1]
                
    #Retorna el subarreglo más largo o None si no se encuentra ninguno.
    if max_tamaño == 0:
        return None  
    return arreglo_maximo

        
    
