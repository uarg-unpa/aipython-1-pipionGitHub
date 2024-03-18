#creacion de lista usando metodo
#nombres=list()
#crar lista con valores inciales
nombres=list(['pipi','tosito','pookie'])
print(nombres)
#metodos, append, permite agregar un elemento al finla de la lista
nombres.append('carlos')
print(nombres)
#insert
print()
nombres.insert(0,'annie')
print(nombres)
#utilizar el operador in
for nombre in nombres:
    print(nombre)

#mutabilidad
print()
nombres[4]='normis'
for nombre in nombres:
    print(nombre)






