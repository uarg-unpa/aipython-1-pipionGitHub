e1=int(input("Ingrese su edad: "))
e2=int(20)
if e1 == e2:
    print("ayyy gemelaas 😍") 
else:
    if e1 < e2:
        dif=e2-e1
        if dif == 1:
            print(f"Yo soy más grande por {dif} año 😈")
        else:
            print(f"Yo soy más grande por {dif} años 😈")
    else:
        dif=e1-e2
        if dif == 1:
            print(f"Vos sos más grande que yo por {dif} año 😔")
        else:
            print(f"Vos sos más grande que yo por {dif} años 😔")