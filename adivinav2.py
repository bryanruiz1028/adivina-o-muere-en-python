
def juego():   
    import random
    intentos=10
    limite=100
    adivina = random.randint(1,limite)
    print(f"tienes {intentos} intentos")
    numero =int(input(f"intrusca un numero del 1 al {limite}  :"))
    while intentos==10 or intentos==9 or intentos==8 or intentos ==7 or intentos==6 or intentos==5 or intentos==4 or intentos==3 or intentos==2  :
        if adivina==numero:
            print ("FELICIDADES ACERTASTE ")
            break # con esto ponemos final al while
        elif adivina>numero:
            print("es un numero muy bajo")
            intentos=intentos-1
            print(f"te quedan {intentos} intentos")
            numero =int(input("intrusca un numero del 1 al 100  :"))
            if intentos==1:
                print("ya no tienes mas intentos ")        
        else:
            print("numero muy alto")
            intentos=intentos-1
            print(f"te quedan {intentos} intentos")
            numero =int(input("intrusca un numero del 1 al 100  :"))
            if intentos==1:
                print("ya no tienes mas intentos ")
                print(f"PERDISTE  el numero era {adivina}")
    print("FIN DEL JUEGO")
a=1
while a==1:
    print("presione 1 para  jugar ")
    print("presione otra tecla para salir")
    friv =int(input(">"))
    if friv==1:
        juego()
    else:
        print("chao")
        break