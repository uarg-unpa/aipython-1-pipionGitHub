#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión.
inv=int(input("Ingrese la cantidad que desea invertir: "))
tna=float(input("Ingrese el valor de la tasa nominal anual: "))
anios=int(input("Ingrese la cantidad de años que desea invertir: "))

interes=float((inv*tna)/100)

print("El total de su inversión es el siguiente: ",interes*anios+inv)