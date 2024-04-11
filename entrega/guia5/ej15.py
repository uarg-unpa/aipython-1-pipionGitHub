def promedioLista(lista):
    suma = 0
    promedio = float(0)
    for i in lista:
        suma = suma + i
    promedio = suma / len(lista)
    return promedio

nums=[1,2,3,4,5]
print(nums)
print(promedioLista(nums))
