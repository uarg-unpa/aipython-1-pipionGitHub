psw=input("Ingrese su contraseña para ser guardada: ")
psw2=input("Ingrese la contraseña nuevamente para verificar si es correcta: ")
if psw == psw2:
    print("La contraseña es correcta.")
else:
    if psw2.upper() == psw:
        print("La contraseña es correcta. ")
    else:
        if psw2.lower() == psw:
            print("La contraseña es correcta. ")
        else:
            if psw.upper() == psw2:
                print("La contraseña es correcta. ")
            else:
                if psw.lower() == psw2:
                    print("La contraseña es correcta. ")
                else:
                    print("La contraseña es incorrecta. ")