palabra = input("Favor de ingresar una palabra: ")

s = list(palabra.lower())
if s == list(reversed(s)):
    print ("La palabra es palindroma")

else:
    print("Muerase")
