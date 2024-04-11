num = int(input("Ingrese un número entero positivo mayor a 3: "))
n = int(1)

while n <= num:
    if num < 3:
        print("El número que ha ingresado es inválido. ")
    else:
        if n % 2 == 1:
            print(n)
    n = n + 1