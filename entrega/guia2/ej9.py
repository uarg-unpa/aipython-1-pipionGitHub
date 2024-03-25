age=int(input("Ingrese su edad: "))
ing=int(input("Ingrese sus ingresos mensuales: "))

if age < 0:
    print("Todavía ni naciste. ")
elif age < 18:
    print("Usted no tiene q pagar el impuesto ya que es menor de edad. ")
elif age > 17 and ing < 100000:
    print("Usted no debe pagar el impuesto, su salario es inferior a $100.000 mensuales. ")
else:
    print("Usted sí debe pagar el impuesto. ")