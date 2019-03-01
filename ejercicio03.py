num1 = input('Favor de ingresar el primer numero')
num2 = input('Favor de ingresar el segundo numero')

while (num1 and num2 != 0)
    if num1 > num2:
        print('El numero mayor es:\t',num1)
    elif num2 > num1:
        print('El numero mayor es:\t',num2)
    else:
        break
