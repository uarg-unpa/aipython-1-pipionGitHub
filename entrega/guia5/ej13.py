def vocales(lista):
    cantVocales=0
    for v in lista:
        if v == 'a'or v == 'e' or v == 'i'or v == 'o' or v == 'u':
            cantVocales = cantVocales + 1
    return cantVocales

lista = list("asxcvbhtrewsdcvbn")
print(lista)
print(vocales(lista))


