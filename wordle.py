#Posibles palabras que pueden salir en wordle "importando random"
import random

posibles_palabras = ["autos","silla","mesas","manos"]

palabra_secreta = random.choice(posibles_palabras)

while intentos <= 6:

    letras_verificadas = []
    cantidad_letras = 5

    #SE PIDE AL USUARIO INGRESAR UNA PALABRA

    palabra_ingresada = input("Ingrese una palabra: ")

    
    
    intentos += 1