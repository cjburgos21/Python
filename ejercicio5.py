a = [1,5,8,21,12]
b = [7,1,9,12,22]

num = int(input("Favor de ingresar un numero: "))

same = []

for num1 in a:
    for num2 in b:
        if num1 != num2: continue
        if  num1 in same == True: continue

    same.append(num1)


    print("la primera y segunda listas son: " + a +b)
        if same == []:
        print("no hay elementos comunes en ambas listas")

    else:
        print("los numeros en comun son los siguientes: "+ same)
