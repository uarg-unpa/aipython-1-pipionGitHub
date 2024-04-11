
lista = [1, 2, 3, 4]
lista1 = [5, 6, 7, 8]
result = []

def intercalar(l1, l2):
    for a, b in zip(l1, l2):
        result.append(a)
        result.append(b)
    return result
       
print(intercalar(lista, lista1))