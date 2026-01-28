#Posibles palabras que pueden salir en wordle "importando random"
import random

posibles_palabras = ["autos","silla","mesas","manos"]

palabra_secreta = random.choice(posibles_palabras)

while intentos <= 6:

    #SE PIDE AL USUARIO INGRESAR UNA PALABRA

    palabra_ingresada = input("Ingrese una palabra: ")

    #VERIFICAR QUE LA PALABRA INGRESADA TIENE 5 CARACTERES
    while len(palabra_ingresada) != cantidad_letras:
        print("Intente ingresar una palabra de 5 caracteres... ")
        palabra_ingresada = input("Ingrese una palabra: ")
    


    
    
    intentos += 1