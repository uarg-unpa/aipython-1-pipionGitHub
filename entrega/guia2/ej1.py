age=int(input("Ingrese su edad: "))

if age > 17:
    print("Tiene edad suficiente para conducir. ")
else:
    if age < 0:
        print("La edad que usted ingresó es inválida. ")
    else:
        falta=18-age
        print(f"No tiene edad suficiente para conducir. Le faltan {falta} años. ")
