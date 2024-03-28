

def deFarenjeiaCelcius(gradosf):
    cel = float(gradosf - 32) * (5/9)
    return cel

far = int(input("Ingrese los grados farenheit para convertirlos a celcius: "))
print(deFarenjeiaCelcius(far))