lista = [1,3,12,7,4,24,12,9,10,117]
num = int(input("Escoja un numero del listado: "))
nueva_lista = []
for i in lista:
    if i < num:
        nueva_lista.append(i)

print (nueva_lista)
