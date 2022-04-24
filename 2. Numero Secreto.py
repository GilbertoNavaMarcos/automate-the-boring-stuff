# Adivina el numerito

import random

print('Adivina el numero')

numero_secreto = random.randint(1,10)

print('Intenta adivinar el numero. El rango es de 1 a 10')

# 3 intentos para adivinar el numero

for intento in range(3):
    print('Intento', intento + 1)
    numero_usuario = int(input())
    
    if numero_usuario < numero_secreto:
        print('El numero es mayor')
    if numero_usuario > numero_secreto:
        print('El numero es menor')
    
if numero_usuario == numero_secreto:
        print('Felicidades, adivinaste el numero')
else: 
    print('Lo siento, no adivinaste el numero')
    print('El numero era', numero_secreto)