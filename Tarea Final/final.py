import random

#def rollDice(sides):
#        return random.randint(1, sides) // single roll, very much unnecessary

def singleRoll(dices, sides):
    results = []
    for i in range(dices):
        #print(f"Dice {i+1}: {rollDice(sides)}")
        #results.append(rollDice(sides))
        results.append(random.randint(1, sides))
    return results

def rollDices(rolls, dices, sides):
    resultList = []
    if rolls < 2:
        singleRoll(dices, sides)
    else: 
        for i in range (rolls):
            #singleRoll(dices, sides)
            resultList.append(singleRoll(dices, sides))
        return resultList

def pickSides():
    sides = int(input("Seleccione la cantidad de caras del dado: "))
    correct = False
    while correct == False:
        if sides !=6 and sides !=8 and sides !=10 and sides !=12:
            print("La cantidad de caras seleccionada es incorrecta.","recuerde: solo puede elegir dados de 6, 8, 10 y 12 caras. ",sep="\n")
            sides = int(input("Por favor, elija de nuevo: "))
        else:
            correct = True
    return sides

def pickDices():
    dices = int(input("Indique la cantidad de dados que desea lanzar: "))
    correct = False
    while correct == False:
        if dices != 1 and dices !=2 and dices !=4 and dices !=6:
            print("La centidad de dados que eligió lanzar es incorrecta.","Recuerde: solo puede lanzar 1, 2, 4 o 6 dados al mismo tiempo. ",sep="\n")
            dices = int(input("Por favor, elija nuevamente: "))
        else:
            correct = True
    return dices

def pickRolls():
    rolls = int(input("Indique la cantidad de tiros que desea lanzar. "))
    correct = False
    while correct == False:
        if rolls !=2 and rolls !=3 and rolls !=4 and rolls !=1:
            print("La cantidad de tiros que indicó es incorrecta.","Recuerde: solo puede lanzar 2, 3, 4 o 6 tiros por turno. ",sep="\n")
            rolls = int(input("Porfis, elija nuevamente: "))
        else:
            correct = True
    return rolls

def rollScore(resultList):
    score = 0 
    totalScore = 0
    l = 0
    for i in resultList:
        l = l + 1
        for j in i:
            score = score + j
        print(f"Puntaje del lanzamiento {l}: {score}")
        totalScore = totalScore + score
        score = 0
    print(f"Puntaje total del turno: {totalScore}")

def showOptions():
    print("1. Tirar los dados. ")
    print("2. Ver estadísticas. ")
    #print("3. Jugar Pipi's DiceLand Adventure. ")
    print("4. Salir. ")

def statistics(rolls, dices, sides, resultlist):
    print(f"Lanzamientos: {rolls}. \nDados lanzados: {dices}. \nTipo de dado: {sides} caras. \n")
    rollScore(resultlist)

def menu():
    print("Tirá tus daditos, estas son tus opciones: \n")
    end = False
    rolls = 0
    dices = 0
    sides = 0
    results = 0
    while end == False:
        showOptions()
        print()
        option = int(input("Qué opción desea realizar? "))
        match(option):
            case 1:
                rolls = pickRolls()
                dices = pickDices()
                sides = pickSides()
                results = rollDices(rolls, dices, sides)
                print(f"Resultados del turno: {results}")
                r = (input("¿Desea volver al menú? \n"))
                if r != 'si' and r != 'Si' and r != 'chi' and r != 'Sí' and r != 'sí':
                    end = True
                print()
            case 2:
                statistics(rolls, dices, sides, results)
                print()
            case _:
                print("Bye Bye! Thank u for playing <3 ")
                end = True
menu()

