print("Bienvenidos a piedra, papel o tijeras...")

P1 = input("Ingrese su eleccion ")

P2 = input("Ahora usted ")

def compare(P1, P2):
    if P1 == P2:
        print("Empate...")
    elif P1 == 'piedra':
        if P2 == 'tijeras':
            print("Gano el P1")
        else:
            print("Gana el P2")
    elif P1 == 'tijeras':
        if P2 == 'papel':
            print("Gano el P1")
        else:
            print("Gana el P2")
    elif P1 == 'papel':
        if P2 == 'piedra':
            print("Gana el P1")
        else:
            print("Gana el P2")

    else:
        return("Valores ingresados invalidos prueben otra vez")
        sys.exit(0)

        print (compare(P1, P2))
