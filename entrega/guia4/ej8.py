def invertirString(palabra):
    result = ""
    for l in palabra:
        result = l + result
    return result

pal = input("Ingrese una palabra para invertir uwu - ")
print(invertirString(pal))