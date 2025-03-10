import os
import time
from colorama import Fore, Back, Style
esp = ''
voc = ['á', 'é', 'í', 'ó', 'ú']

def pantalla():
    print(Fore.BLUE + ''' 
    *********************************************************
                  TRADUCTOR DE ROSARIGASINO
    .- Ingresá un texto para traducigacirlo.
    !- Fijate de colocarle una tilde a la vocal acentuada de 
       cada palabra''' + Fore.RED + '''
       Ej. 'Silla' no lleva tilde, pero debes escribir 'Sílla' ''' 
       + Fore.BLUE +'''
    .- Ingresá '0' para salir   
    @ created by judibot :) - industria rosarigasina
    *********************************************************
    ''')

def traducir(org):
    pos = -1                                                    # Buscar la primera vocal
    for i, al in enumerate(org):
        if al in voc:
            pos = i
            break                                                   # Si hay vocal modificar la palabra
    if pos != -1:
        ros = org[:pos] + org[pos] + 'gas' + org[pos:] 
        return ros                      # Devuelve la nueva palabra
    else:
        return org                      # Si no hay vocal, devuelve la original

pantalla()                              
while esp != '0':
    esp = input('Ingresá una palagasabra: ')
    ros = ""

    for j in esp.split():                                           # Dividir el texto en palabras sin guardarlas en una lista
        ros += traducir(j) + " "                                    # Traducir cada palabra y agregarla

    print(ros.strip())                                          
os.system('cls')
print(Fore.GREEN + '--- @ created by judibot :) - industria rosarigasina ---')
time.sleep(4)
