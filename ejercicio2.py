name = input("Favor de ingresar su nombre:")
print("Bienvenido "+ name)
num = int(input("Favor de ingresar primer digito:"))
print("Digito guardado...")
check = int(input("Favor de ingresar segundo digito"))
print("Digito guardado...")
if num % 2 == 0:
    print(num, "Es par")

elif check == 0:
    print(name + " la division no puede efectuarse")

else:
    print(num, "Es primo")
