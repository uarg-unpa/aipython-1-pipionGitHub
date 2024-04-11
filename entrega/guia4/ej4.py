def tablaM(num):
    for i in range(10):
        print(f"{num} x {i+1} = {num * (i+1)}")

n=int(input("Ingrese un número entero. "))
print(tablaM(n))