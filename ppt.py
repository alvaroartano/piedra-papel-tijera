#imports
import os
import sys
from termcolor import colored
import random
import keyboard

#vacíar la terminal
os.system('clear')



#bienvenida
print('')
print(colored('Bienvenido a', 'white'), colored('piedra,', 'red'), colored('papel o', 'yellow'), colored('tijera', 'cyan'))
print(colored('𝖒𝖆𝖉𝖊 𝖇𝖞 @𝖆𝖑𝖛𝖆𝖗𝖔𝖆𝖗𝖙𝖆𝖓𝖔', 'cyan'))
print('')
enter = input('Pulsa la tecla enter para continuar...')


#funcionamiento
if enter == "":
    os.system('clear')
    assets = ['Piedra', 'Papel', 'Tijera']
    random = assets[random.randint(0, 2)]
    #print(random)
    print('Selecciona una de las opciones de abajo: ')
    print(colored("""
     1 - Piedra
     2 - Papel
     3 - Tijera
    """, 'cyan'))

    eleccion = input(colored("Introduce el número de tu elección: ", 'yellow'))

    #Máquina = Piedra
    if random == 'Piedra' and eleccion == '1':
        os.system('clear')
        print(colored("Habéis quedado empate :)", 'cyan'))
        print('')
        print(f"La elección de la máquina ha sido {random}, y la tuya ha sido Piedra")
        print("")
        terminar = input(colored("Quieres volver a jugar? (y/n): ", "yellow"))
        if terminar == 'y':
            os.system('python3 ppt.py')
        else:
            print("")
            print(colored("Perfecto! Hasta la próxima!", "cyan"))

    if random == 'Piedra' and eleccion == '2':
        os.system('clear')
        print(colored("Has ganado! :)", 'cyan'))
        print('')
        print(f"La elección de la máquina ha sido {random}, y la tuya ha sido Papel")
        print("")
        terminar = input(colored("Quieres volver a jugar? (y/n): ", "yellow"))
        if terminar == 'y':
            os.system('python3 ppt.py')
        else:
            print("")
            print(colored("Perfecto! Hasta la próxima!", "cyan"))

    if random == 'Piedra' and eleccion == '3':
        os.system('clear')
        print(colored("Has perdido! :(", 'cyan'))
        print('')
        print(f"La elección de la máquina ha sido {random}, y la tuya ha sido Tijera")
        print("")
        terminar = input(colored("Quieres volver a jugar? (y/n): ", "yellow"))
        if terminar == 'y':
            os.system('python3 ppt.py')
        else:
            print("")
            print(colored("Perfecto! Hasta la próxima!", "cyan"))


    #Máquina = Papel
    if random == 'Papel' and eleccion == '1':
        os.system('clear')
        print(colored("Has perdido! :(", 'cyan'))
        print('')
        print(f"La elección de la máquina ha sido {random}, y la tuya ha sido Piedra")
        print("")
        terminar = input(colored("Quieres volver a jugar? (y/n): ", "yellow"))
        if terminar == 'y':
            os.system('python3 ppt.py')
        else:
            print("")
            print(colored("Perfecto! Hasta la próxima!", "cyan"))

    if random == 'Papel' and eleccion == '2':
        os.system('clear')
        print(colored("Habéis quedado empate! :)", 'cyan'))
        print('')
        print(f"La elección de la máquina ha sido {random}, y la tuya ha sido Papel")
        print("")
        terminar = input(colored("Quieres volver a jugar? (y/n): ", "yellow"))
        if terminar == 'y':
            os.system('python3 ppt.py')
        else:
            print("")
            print(colored("Perfecto! Hasta la próxima!", "cyan"))

    if random == 'Papel' and eleccion == '3':
        os.system('clear')
        print(colored("Has ganado! :)", 'cyan'))
        print('')
        print(f"La elección de la máquina ha sido {random}, y la tuya ha sido Tijera")
        print("")
        terminar = input(colored("Quieres volver a jugar? (y/n): ", "yellow"))
        if terminar == 'y':
            os.system('python3 ppt.py')
        else:
            print("")
            print(colored("Perfecto! Hasta la próxima!", "cyan"))


    #Máquina = Tijeras
    if random == 'Tijera' and eleccion == '1':
        os.system('clear')
        print(colored("Has ganado! :(", 'cyan'))
        print('')
        print(f"La elección de la máquina ha sido {random}, y la tuya ha sido Piedra")
        print("")
        terminar = input(colored("Quieres volver a jugar? (y/n): ", "yellow"))
        if terminar == 'y':
            os.system('python3 ppt.py')
        else:
            print("")
            print(colored("Perfecto! Hasta la próxima!", "cyan"))

    if random == 'Tijera' and eleccion == '2':
        os.system('clear')
        print(colored("Has perdido! :(", 'cyan'))
        print('')
        print(f"La elección de la máquina ha sido {random}, y la tuya ha sido Papel")
        print("")
        terminar = input(colored("Quieres volver a jugar? (y/n): ", "yellow"))
        if terminar == 'y':
            os.system('python3 ppt.py')
        else:
            print("")
            print(colored("Perfecto! Hasta la próxima!", "cyan"))

    if random == 'Tijera' and eleccion == '3':
        os.system('clear')
        print(colored("Habéis quedado empate! :)", 'cyan'))
        print('')
        print(f"La elección de la máquina ha sido {random}, y la tuya ha sido Tijera")
        print("")
        terminar = input(colored("Quieres volver a jugar? (y/n): ", "yellow"))
        if terminar == 'y':
            os.system('python3 ppt.py')
        else:
            print("")
            print(colored("Perfecto! Hasta la próxima!", "cyan"))