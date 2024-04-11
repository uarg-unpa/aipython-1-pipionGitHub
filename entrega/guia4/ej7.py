def numeroMayor(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

print("Ingrese tres números para compararlos: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())
print(f"De los npumeros ingresados, el mayor es el {numeroMayor(num1, num2, num3)}")