def invertirString(palabra):
    result = ""
    for l in palabra:
        result = l + result
    return result

def palindromo(palabra):
    palin = False
    if palabra == invertirString(palabra):
        palin = True
        return palin
    else:
        return palin

pal = input("Ingresa una palabra para chequear si es palíndromo o no: ")

if palindromo(pal) == True:
    print(f"La palabra ingresada sí es un palíndromo. ")
else:
    print("La palabra ingresada no es un palíndromo. ")