def parImpar(num):
    if num % 2 == 0:
        p = "par"
        return p
    else:
        p = "impar"
        return p

n=int(input("Ingrese un numero entero: "))
print(f"El número que usted ingresó es {parImpar(n)}")
