# Funciones del sistema operativo
import os
# Se importa rutina sleep para permitir desplegar mensajes por un tiempo definido
from time import sleep
# Definición de Variables Globales
V=[] # Se utiliza para almacenar la lista de videos
I=-1 # Se utiliza para registrar la cantidad de videos guardados en la lista menos uno, si contiene -1 implica que no hay videos en la lista
DirectorioRelativo=""
def IngreseNumero(UnTexto,Min,Max):
    # Esta funcion se utiliza para que el usuario ingrese un número comprendido en el rango Min y Max
    # devuelve dos valores, el primer valor es el número ingresado por el usuario, y el segúndo valor es booleano e indica si 
    # el valor ingresado por el usuario es válido o no, colocando Verdadero para valores válidos y Falso para valores inválidos
    Logro = False
    UnNumero=0
    try:
        UnDato=int(input(UnTexto))
    except:
        print("Por favor, ingrese un número")
        sleep(5)
    else:
        if UnDato>=Min and UnDato<=Max:
           UnNumero=UnDato
           Logro = True
    return UnNumero,Logro    

def CS():
    # Esta función se utiliza para limpiar la pantalla
    # para lo que es necesario evaluar si el sistema operativo es windows (nt) o linux
    if(os.name =='nt'):
        os.system('cls')
    else:
        os.system('clear')
