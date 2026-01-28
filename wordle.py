#Posibles palabras que pueden salir en wordle "importando random"
import random

posibles_palabras = ["autos","silla","mesas","manos"]

palabra_secreta = random.choice(posibles_palabras)

while intentos <= 6:

    letras_verificadas = []

    cantidad_letras = 5

    #SE PIDE AL USUARIO INGRESAR UNA PALABRA

    palabra_ingresada = input("Ingrese una palabra: ")

    #VERIFICAR QUE LA PALABRA INGRESADA TIENE 5 CARACTERES
    while len(palabra_ingresada) != cantidad_letras:
        print("Intente ingresar una palabra de 5 caracteres... ")
        palabra_ingresada = input("Ingrese una palabra: ")

    #VERIFICAR LAS LETRAS DENTRO DE LA PALABRA

    for i in range(cantidad_letras):
        las_palabras_son_iguales = palabra_ingresada[i] == palabra_secreta[i] # True o False
        la_letra_existe_en_la_palabra = palabra_ingresada[i] in palabra_secreta 
        
        if las_palabras_son_iguales:
              letras_verificadas.append(f"[{palabra_ingresada[i]}]")
        elif la_letra_existe_en_la_palabra:
                letras_verificadas.append(f"({palabra_ingresada[i]})")
        else:
                letras_verificadas.append(palabra_ingresada[i])

    
    intentos += 1