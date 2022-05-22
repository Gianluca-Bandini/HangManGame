#Gianluca de la Rosa Bandini A01736162
#Juego de Ahorcado para ayudar a alumnos a estudiar el apartado de ciencias para la evaluación PISA 

import random
archivo = open("T13_Palabras.txt", "r")
linea1 = archivo.readline()
linea2 = archivo.readline()
linea3 = archivo.readline()
linea4 = archivo.readline()
linea5 = archivo.readline()
linea6 = archivo.readline()
linea7 = archivo.readline()
linea8 = archivo.readline()
linea9 = archivo.readline()
linea10 = archivo.readline()
linea11 = archivo.readline()
linea12 = archivo.readline()
linea13 = archivo.readline()
linea14 = archivo.readline()
linea15 = archivo.readline()
linea16 = archivo.readline()
linea17 = archivo.readline()
linea18 = archivo.readline()
linea19 = archivo.readline()
linea20 = archivo.readline()

adivinanza_a_elegir = random.randint(1,20)
vidas = 5

print("¡¡¡Bienvenido al juego de Ahorcado para estudiar para la evaluación de PISA!!!")
print("Este juego se basa principalmente en el apartado de CIENCIAS")
print("Estas preguntas fueron creadas tomando en cuenta evaluaciones pasadas de PISA")
print("Tendrás 5 vidas para contestar")
print("FAVOR DE PONER LAS LETRAS EN MAYÚSCULA Y SIN ACENTO")
print("¡¡¡DIVIÉRTETE!!!")


if adivinanza_a_elegir == 1:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_", "_","_"]
    print("Esta palabra tiene 9 letras")
    print ("Al ponerle cloro al agua ¿Qué se intenta matar?")
    while vidas > 0 and palabra_a_adivinar != ["B","A","C","T","E","R","I","A","S"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "B":
                    palabra_a_adivinar[0] = "B"
                elif letra == "A":
                    palabra_a_adivinar[1] = "A"
                    palabra_a_adivinar[7] = "A"
                elif letra == "C":
                    palabra_a_adivinar[2] = "C"
                elif letra == "T":
                    palabra_a_adivinar[3] = "T"
                elif letra == "E":
                    palabra_a_adivinar[4] = "E"
                elif letra == "R":
                    palabra_a_adivinar[5] = "R"
                elif letra == "I":
                    palabra_a_adivinar[6] = "I"
                elif letra == "S":
                    palabra_a_adivinar[8] = "S"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["B","A","C","T","E","R","I","A","S"]:
        print(["B","A","C","T","E","R","I","A","S"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea1)

elif adivinanza_a_elegir == 2:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_", "_","_"]
    print("Esta palabra tiene 9 letras")
    print("¿Qué vitamina no tiene el chocolate?:")
    while vidas > 0 and palabra_a_adivinar != ["V","I","T","A","M","I","N","A","C"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "V":
                    palabra_a_adivinar[0] = "V"
                elif letra == "I":
                    palabra_a_adivinar[1] = "I"
                    palabra_a_adivinar[5] = "I"
                elif letra == "T":
                    palabra_a_adivinar[2] = "T"
                elif letra == "A":
                    palabra_a_adivinar[3] = "A"
                    palabra_a_adivinar[7] = "A"
                elif letra == "M":
                    palabra_a_adivinar[4] = "M"
                elif letra == "N":
                    palabra_a_adivinar[6] = "N"
                elif letra == "C":
                    palabra_a_adivinar[8] = "C"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["V","I","T","A","M","I","N","A","C"]:
        print (["V","I","T","A","M","I","N","A","C"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea2)

elif adivinanza_a_elegir == 3:
    palabra_a_adivinar = ["_", "_", "_", "_", "_"]
    print("Esta palabra tiene 5 letras")
    print("A través del tiempo los caballos han evolucionado ¿Que parte de su cuerpo existe pero con menor número?:")
    while vidas > 0 and palabra_a_adivinar != ["D","E","D","O","S"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "D":
                    palabra_a_adivinar[0] = "D"
                    palabra_a_adivinar[2] = "D"
                elif letra == "E":
                    palabra_a_adivinar[1] = "E"
                elif letra == "O":
                    palabra_a_adivinar[3] = "O"
                elif letra == "S":
                    palabra_a_adivinar[4] = "S"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["D","E","D","O","S"]:
        print (["D","E","D","O","S"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea3)

elif adivinanza_a_elegir == 4:
    palabra_a_adivinar = ["_", "_", "_"]
    print("Esta palabra tiene 3 letras")
    print("La razón por la que hay dia y noche, es porque la Tierra gira alrededor de su:")
    while vidas > 0 and palabra_a_adivinar != ["E","J","E"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "E":
                    palabra_a_adivinar[0] = "E"
                    palabra_a_adivinar[2] = "E"
                elif letra == "E":
                    palabra_a_adivinar[1] = "J"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["E","J","E"]:
        print (["E","J","E"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea4)

elif adivinanza_a_elegir == 5:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_", "_","_", "_"]
    print("Esta palabra tiene 10 letras")
    print("¿En dónde se forma el ozono malo después de una tormenta eléctrica?:")
    while vidas > 0 and palabra_a_adivinar != ["T","R","O","P","O","S","F","E","R","A"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "T":
                    palabra_a_adivinar[0] = "T"
                elif letra == "R":
                    palabra_a_adivinar[1] = "R"
                    palabra_a_adivinar[8] = "R"
                elif letra == "O":
                    palabra_a_adivinar[2] = "O"
                    palabra_a_adivinar[4] = "O"
                elif letra == "P":
                    palabra_a_adivinar[3] = "P"
                elif letra == "S":
                    palabra_a_adivinar[5] = "S"
                elif letra == "F":
                    palabra_a_adivinar[6] = "F"
                elif letra == "E":
                    palabra_a_adivinar[7] = "E"
                elif letra == "A":
                    palabra_a_adivinar[9] = "A"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["T","R","O","P","O","S","F","E","R","A"]:
        print (["T","R","O","P","O","S","F","E","R","A"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea5)

elif adivinanza_a_elegir == 6:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_", "_"]
    print("Esta palabra tiene 8 letras")
    print("¿Qué previene hacer el ejercicio y es uno de los mayores problemas en México?:")
    while vidas > 0 and palabra_a_adivinar != ["O","B","E","S","I","D","A","D"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "O":
                    palabra_a_adivinar[0] = "O"
                elif letra == "B":
                    palabra_a_adivinar[1] = "B"
                elif letra == "E":
                    palabra_a_adivinar[2] = "E"
                elif letra == "S":
                    palabra_a_adivinar[3] = "S"
                elif letra == "I":
                    palabra_a_adivinar[4] = "I"
                elif letra == "D":
                    palabra_a_adivinar[5] = "D"
                    palabra_a_adivinar[7] = "D"
                elif letra == "A":
                    palabra_a_adivinar[6] = "A"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["O","B","E","S","I","D","A","D"]:
        print (["O","B","E","S","I","D","A","D"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea6)

elif adivinanza_a_elegir == 7:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_", "_","_"]
    print("Esta palabra tiene 9 letras")
    print("El humo del tabaco es inhalado por los pulmones, pero ¿Qué componente de este humo impide que los pulmones funcionen correctamente?:")
    while vidas > 0 and palabra_a_adivinar != ["A","L","Q","U","I","T","R","A","N"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "A":
                    palabra_a_adivinar[0] = "A"
                    palabra_a_adivinar[7] = "A"
                elif letra == "L":
                    palabra_a_adivinar[1] = "L"
                elif letra == "Q":
                    palabra_a_adivinar[2] = "Q"
                elif letra == "U":
                    palabra_a_adivinar[3] = "U"
                elif letra == "I":
                    palabra_a_adivinar[4] = "I"
                elif letra == "T":
                    palabra_a_adivinar[5] = "T"
                elif letra == "R":
                    palabra_a_adivinar[6] = "R"
                elif letra == "N":
                    palabra_a_adivinar[8] = "N"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["A","L","Q","U","I","T","R","A","N"]:
        print (["A","L","Q","U","I","T","R","A","N"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea7)

elif adivinanza_a_elegir == 8:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_", "_","_", "_", "_"]
    print("Esta palabra tiene 11 letras")
    print("Al vacunarnos el cuerpo genera ¿Qué cosa?:")
    while vidas > 0 and palabra_a_adivinar != ["A","N","T","I","C","U","E","R","P","O","S"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "A":
                    palabra_a_adivinar[0] = "A"
                elif letra == "N":
                    palabra_a_adivinar[1] = "N"
                elif letra == "T":
                    palabra_a_adivinar[2] = "T"
                elif letra == "I":
                    palabra_a_adivinar[3] = "I"
                elif letra == "C":
                    palabra_a_adivinar[4] = "C"
                elif letra == "U":
                    palabra_a_adivinar[5] = "U"
                elif letra == "E":
                    palabra_a_adivinar[6] = "E"
                elif letra == "R":
                    palabra_a_adivinar[7] = "R"
                elif letra == "P":
                    palabra_a_adivinar[8] = "P"
                elif letra == "O":
                    palabra_a_adivinar[9] = "O"
                elif letra == "S":
                    palabra_a_adivinar[10] = "S"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["A","N","T","I","C","U","E","R","P","O","S"]:
        print (["A","N","T","I","C","U","E","R","P","O","S"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea8)

elif adivinanza_a_elegir == 9:
    palabra_a_adivinar = ["_", "_", "_", "_"]
    print("Esta palabra tiene 4 letras")
    print("Los rayos X son malos para las mujeres embarazadas porque pueden dañar al:")
    while vidas > 0 and palabra_a_adivinar != ["F","E","T","O"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "F":
                    palabra_a_adivinar[0] = "F"
                elif letra == "E":
                    palabra_a_adivinar[1] = "E"
                elif letra == "T":
                    palabra_a_adivinar[2] = "T"
                elif letra == "O":
                    palabra_a_adivinar[3] = "O"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["F","E","T","O"]:
        print (["F","E","T","O"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea9)

elif adivinanza_a_elegir == 10:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_"]
    print("Esta palabra tiene 7 letras")
    print("Un catalizador se encarga de transformar componentes como monóxido de carbono en dióxido de:")
    while vidas > 0 and palabra_a_adivinar != ["C","A","R","B","O","N","O"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "C":
                    palabra_a_adivinar[0] = "C"
                elif letra == "A":
                    palabra_a_adivinar[1] = "A"
                elif letra == "R":
                    palabra_a_adivinar[2] = "R"
                elif letra == "B":
                    palabra_a_adivinar[3] = "B"
                elif letra == "O":
                    palabra_a_adivinar[4] = "O"
                    palabra_a_adivinar[6] = "O"
                elif letra == "N":
                    palabra_a_adivinar[5] = "N"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["C","A","R","B","O","N","O"]:
        print (["C","A","R","B","O","N","O"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea10)

elif adivinanza_a_elegir == 11:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_", "_","_"]
    print("Esta palabra tiene 9 letras")
    print("La lluvia ácida tiene principalmente gases como el óxido de azufre y el óxido de:")
    while vidas > 0 and palabra_a_adivinar != ["N","I","T","R","O","G","E","N","O"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "N":
                    palabra_a_adivinar[0] = "N"
                    palabra_a_adivinar[7] = "N"
                elif letra == "I":
                    palabra_a_adivinar[1] = "I"
                elif letra == "T":
                    palabra_a_adivinar[2] = "T"
                elif letra == "R":
                    palabra_a_adivinar[3] = "R"
                elif letra == "O":
                    palabra_a_adivinar[4] = "O"
                    palabra_a_adivinar[8] = "O"
                elif letra == "G":
                    palabra_a_adivinar[5] = "G"
                elif letra == "E":
                    palabra_a_adivinar[6] = "E"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["N","I","T","R","O","G","E","N","O"]:
        print (["N","I","T","R","O","G","E","N","O"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea11)


elif adivinanza_a_elegir == 12:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_"]
    print("Esta palabra tiene 7 letras")
    print("El aire es menos menso al aumentar la:")
    while vidas > 0 and palabra_a_adivinar != ["A","L","T","I","T","U","D"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra ")
        for letra in intento_de_adivinar:
                if letra == "A":
                    palabra_a_adivinar[0] = "A"
                elif letra == "L":
                    palabra_a_adivinar[1] = "L"
                elif letra == "T":
                    palabra_a_adivinar[2] = "T"
                    palabra_a_adivinar[4] = "T"
                elif letra == "I":
                    palabra_a_adivinar[3] = "I"
                elif letra == "U":
                    palabra_a_adivinar[5] = "U"
                elif letra == "D":
                    palabra_a_adivinar[6] = "D"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["A","L","T","I","T","U","D"]:
        print (["A","L","T","I","T","U","D"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea12)
    
elif adivinanza_a_elegir == 13:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_"]
    print("Esta palabra tiene 7 letras")
    print("Al usar energía limpia no se usan combustibles:")
    while vidas > 0 and palabra_a_adivinar != ["F","O","S","I","L","E","S"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "F":
                    palabra_a_adivinar[0] = "F"
                elif letra == "O":
                    palabra_a_adivinar[1] = "O"
                elif letra == "S":
                    palabra_a_adivinar[2] = "S"
                    palabra_a_adivinar[6] = "S"
                elif letra == "I":
                    palabra_a_adivinar[3] = "I"
                elif letra == "L":
                    palabra_a_adivinar[4] = "L"
                elif letra == "E":
                    palabra_a_adivinar[5] = "E"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["F","O","S","I","L","E","S"]:
        print (["F","O","S","I","L","E","S"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea13)

elif adivinanza_a_elegir == 14:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_", "_","_", "_"]
    print("Esta palabra tiene 10 letras")
    print("¿Qué instrumento ayuda a comprobar que un objeto conduce electricidad o no?:")
    while vidas > 0 and palabra_a_adivinar != ["V","O","L","T","I","M","E","T","R","O"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "V":
                    palabra_a_adivinar[0] = "V"
                    palabra_a_adivinar[9] = "V"
                elif letra == "O":
                    palabra_a_adivinar[1] = "O"
                elif letra == "L":
                    palabra_a_adivinar[2] = "L"
                elif letra == "T":
                    palabra_a_adivinar[3] = "T"
                    palabra_a_adivinar[7] = "T"
                elif letra == "I":
                    palabra_a_adivinar[4] = "I"
                elif letra == "M":
                    palabra_a_adivinar[5] = "M"
                elif letra == "E":
                    palabra_a_adivinar[6] = "E"
                elif letra == "R":
                    palabra_a_adivinar[8] = "R"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["V","O","L","T","I","M","E","T","R","O"]:
        print (["V","O","L","T","I","M","E","T","R","O"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea14)

elif adivinanza_a_elegir == 15:
    palabra_a_adivinar = ["_", "_", "_", "_", "_"]
    print("Esta palabra tiene 5 letras")
    print("Entre ___ sea un lente de un telescopio, mayor será la luz que capta:")
    while vidas > 0 and palabra_a_adivinar != ["M","A","Y","O","R"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "M":
                    palabra_a_adivinar[0] = "M"
                elif letra == "A":
                    palabra_a_adivinar[1] = "A"
                elif letra == "Y":
                    palabra_a_adivinar[2] = "Y"
                elif letra == "O":
                    palabra_a_adivinar[3] = "O"
                elif letra == "R":
                    palabra_a_adivinar[4] = "R"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["M","A","Y","O","R"]:
        print (["M","A","Y","O","R"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea15)


elif adivinanza_a_elegir == 16:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_", "_","_"]
    print("Esta palabra tiene 9 letras")
    print("En la noche, la luz de la ciudad dificulta la visibilidad de las:")
    while vidas > 0 and palabra_a_adivinar != ["E","S","T","R","E","L","L","A","S"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "E":
                    palabra_a_adivinar[0] = "E"
                    palabra_a_adivinar[4] = "E"
                elif letra == "S":
                    palabra_a_adivinar[1] = "S"
                    palabra_a_adivinar[8] = "S"
                elif letra == "T":
                    palabra_a_adivinar[2] = "T"
                elif letra == "R":
                    palabra_a_adivinar[3] = "R"
                elif letra == "L":
                    palabra_a_adivinar[5] = "L"
                    palabra_a_adivinar[6] = "L"
                elif letra == "A":
                    palabra_a_adivinar[7] = "A"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["E","S","T","R","E","L","L","A","S"]:
        print (["E","S","T","R","E","L","L","A","S"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea16)

elif adivinanza_a_elegir == 17:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_"]
    print("Esta palabra tiene 7 letras")
    print("Existen dos tipos principales de reproducciones, la sexual y la:")
    while vidas > 0 and palabra_a_adivinar != ["A","S","E","X","U","A","L"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "A":
                    palabra_a_adivinar[0] = "A"
                    palabra_a_adivinar[5] = "A"
                elif letra == "S":
                    palabra_a_adivinar[1] = "S"
                elif letra == "E":
                    palabra_a_adivinar[2] = "E"
                elif letra == "X":
                    palabra_a_adivinar[3] = "X"
                elif letra == "U":
                    palabra_a_adivinar[4] = "U"
                elif letra == "L":
                    palabra_a_adivinar[6] = "L"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["A","S","E","X","U","A","L"]:
        print (["A","S","E","X","U","A","L"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea17)

elif adivinanza_a_elegir == 18:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_", "_"]
    print("Esta palabra tiene 7 letras")
    print("Los tres principales estados de la materia son líquido, sólido y:")
    while vidas > 0 and palabra_a_adivinar != ["G","A","S","E","O","S","O"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "G":
                    palabra_a_adivinar[0] = "G"
                elif letra == "A":
                    palabra_a_adivinar[1] = "A"
                elif letra == "S":
                    palabra_a_adivinar[2] = "S"
                    palabra_a_adivinar[5] = "S"
                elif letra == "E":
                    palabra_a_adivinar[3] = "E"
                elif letra == "O":
                    palabra_a_adivinar[4] = "O"
                    palabra_a_adivinar[6] = "O"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["G","A","S","E","O","S","O"]:
        print (["G","A","S","E","O","S","O"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea18)

elif adivinanza_a_elegir == 19:
    palabra_a_adivinar = ["_", "_", "_", "_", "_", "_"]
    print("Esta palabra tiene 6 letras")
    print("¿Cuál es el apellido del científico que descubrió La Ley Gravitacional Universal?")
    while vidas > 0 and palabra_a_adivinar != ["N","E","W","T","O","N"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "N":
                    palabra_a_adivinar[0] = "N"
                    palabra_a_adivinar[5] = "N"
                elif letra == "E":
                    palabra_a_adivinar[1] = "E"
                elif letra == "W":
                    palabra_a_adivinar[2] = "W"
                elif letra == "T":
                    palabra_a_adivinar[3] = "T"
                elif letra == "O":
                    palabra_a_adivinar[4] = "O"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["N","E","W","T","O","N"]:
        print (["N","E","W","T","O","N"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea19)

else:
    palabra_a_adivinar = ["_", "_", "_"]
    print("Esta palabra tiene 3 letras")
    print("¿Qué proteina compleja está dentro de las células y es el principal constituyente de material genético?:")
    while vidas > 0 and palabra_a_adivinar != ["A","D","N"]:
        print(palabra_a_adivinar)
        print ("Tienes:", vidas)
        intento_de_adivinar = input("Escriba una letra: ")
        for letra in intento_de_adivinar:
                if letra == "A":
                    palabra_a_adivinar[0] = "A"
                elif letra == "D":
                    palabra_a_adivinar[1] = "D"
                elif letra == "N":
                    palabra_a_adivinar[2] = "N"
                else:
                    print("Intenta de nuevo")
                    vidas = (vidas - 1)
    if vidas > 0 and palabra_a_adivinar == ["A","D","N"]:
        print (["A","D","N"])
        print("¡¡¡Felicidades ganaste!!!")
    else:
        print("Lo siento perdiste, la palabra era: ", linea20)

archivo.close()
