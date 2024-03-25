nota=int(input("Ingrese su puntuación: "))

if nota > 79 and nota < 101:
    print("Clasificación: A")
elif nota > 69 and nota < 80:
    print("Clasificación: B")
elif nota > 59 and nota < 70:
    print("Clasificación: C")
elif nota > 49 and nota < 60:
    print("Clasificación: D")
elif nota >= 0 and nota < 50:
    print("Clasificación: F")