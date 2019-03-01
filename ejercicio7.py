a = [1,2,4,9,12,54,10,82,92,100]

b = []

for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        print ("no hay numeros pares en la lista")


""" Solucion en una linea """

a = [9,12,7,81,12,53,90,5,2,8]
b = [number for number in a if number % 2 == 0]
print (b)
