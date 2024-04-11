print("Ingrese dos números para ser comparados: ")
numa=input()
numb=input()

if numa == numb:
    print(f"{numa} y {numb} son igualitos. ")
else:
    if numa < numb:
        print(f"{numa} es menor que {numb}")
    else:
        print(f"{numa} es mayor que {numb}")
        