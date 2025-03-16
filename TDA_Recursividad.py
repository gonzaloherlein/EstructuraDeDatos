arr1 = [5, 10, 24, 9, 8, 6, 21]

def tieneRepetidos(array):
    if len(array) <= 1:
        return False
    if array[0] in array[1:]:
        return True
    return tieneRepetidos(array[1:])

def nVecesOMas(arreglo,buscado,n):
    if not arreglo:
        return n <= 0
    if arreglo[0] == buscado:
        return nVecesOMas(arreglo[1:],buscado,n - 1)
    return nVecesOMas(arreglo[1:],buscado,n)

def contar_fruta(arreglo,fruta):
    if not arreglo:
        return 0
    if arreglo[0] == fruta:
        return 1 + contar_fruta(arreglo[1:],fruta)
    return contar_fruta(arreglo[1:],fruta)

def perasBananas(arreglo):
    cantidad_peras = contar_fruta(arreglo,"pera")
    cantidad_bananas = contar_fruta(arreglo,"banana")
    return cantidad_peras > cantidad_bananas

def esReverso(arreglo1,arreglo2):
    if len(arreglo1) == 1 and len(arreglo2) == 1:
        return arreglo1[0] == arreglo2[0]
    if len(arreglo1) != len(arreglo2):
        return False
    if arreglo1[0] != arreglo2[-1]:
        return False
    return esReverso(arreglo1[1:],arreglo2[:-1])

def simetricos(arr1,arr2):
    if len(arr1) == 1 and len(arr2) == 1:
        return arr1[0] == arr2[0]
    if arr1[0] != arr2[-1]:
        return False
    return simetricos(arr1[1:],arr2[:-1])

def cantidadPrimos(arreglo):
    cantPrimos = 0 # primos son los numeros que son divisibles por 1 y por si mismos
    if not arreglo:
        return 0
    if esPrimo(arreglo[0]):
        cantPrimos += 1
    return cantPrimos + cantidadPrimos(arreglo[1:])
    
def esPrimo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False  # Los números pares mayores que 2 no son primos
    
    for divisor in range(3, int(n ** 0.5) + 1, 2):  # Verifica solo impares hasta √n
        if n % divisor == 0:
            return False
    return True

def esPar(unNumero:int)->bool:
  return unNumero%2 == 0

def cantNumerosPares(arreglo,cantPares = 0):
    if len(arreglo) == 1:
        if esPar(arreglo[0]):
          cantPares += 1  
    else:
        if esPar(arreglo[0]):
            cantPares += 1
        cantPares = cantNumerosPares(arreglo[1:],cantPares)
    return cantPares
    
def cantNumerosMayoresADiez(arreglo,cantMayoresADiez = 0):
    if len(arreglo) == 1:
        if arreglo[0] > 10:
            cantMayoresADiez += 1
    else:
        if arreglo[0] > 10:
            cantMayoresADiez += 1
        cantMayoresADiez = cantNumerosMayoresADiez(arreglo[1:],cantMayoresADiez)
    return cantMayoresADiez

def masParesQue10(arr1):
    cantPares = cantNumerosPares(arr1)
    cantMayoresADiez = cantNumerosMayoresADiez(arr1)
    return cantPares > cantMayoresADiez
    

print(masParesQue10(arr1))