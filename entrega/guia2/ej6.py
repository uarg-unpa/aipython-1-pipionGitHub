dia=int(input("Ingrese un número para indicar un día de la semana: "))

if dia < 1:
    print("El número ingresado es incorrecto, no corresponde a ningún día. ")
elif dia > 7:
    print("El número ingresado es incorrecto, no corresponde a ningún día. ")

match dia:
    case 1: print(f"El día {dia} corresponde a Lunes. ")
    case 2: print(f"El día {dia} corresponde a Martes. ")
    case 3: print(f"El día {dia} corresponde a Miércoles. ")
    case 4: print(f"El día {dia} corresponde a Jueves. ")
    case 5: print(f"El día {dia} corresponde a Viernes. ")
    case 6: print(f"El día {dia} corresponde a Sábado. ")
    case 7: print(f"El día {dia} corresponde a Domingo. ")