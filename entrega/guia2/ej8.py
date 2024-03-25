age=int(input("Ingrese su edad: ")) 
#Si el cliente es menor de 4 años puede entrar gratis,
#si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, $10.
if age < 0:
    print("La edad ingresada es inválida. ")
elif age < 4:
    print("Puede entrar gratis. ")
elif age > 4 and age < 18:
    print("Su entrada cuesta $5. ")
elif age > 18:
    print("Su entrada cuesta $10. ")
