#Importaciones
from operator import truediv
from pickle import FALSE, TRUE
import webbrowser
import requests
import json
import os
#Importación de la función creada en el archivo SubirArchivosGitHub
from SubirArchivosGitHub import *

#Esta función devuelve la tarea de la semana al recibir el numero de seman como parámetro
def GetHomeWork(SemanaN,FilePath):
    Enlace="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enlace, new=2)
    response=requests.get(Enlace).text
    if response=="El Key introducido es invalido o aun no esta disponible":
        print("Para esta semana no hay contenido")
        exit()
    else: 
        response_info=json.loads(response)
        #Comprobar y manejar la apertura del archivo de recepción
        try:
            archivo=open(FilePath,"w")
        except:
            print("No se pudo crear o abrir el archivo: "+ FilePath)
            exit()
        #Comprobar y manejar tanto la conversión del json a string como la apertura del archivo de recepción
        try:    
            json.dump(response_info,archivo,indent=6)
        except:
            print("El script JSON no fue insertado en el archivo exitosamente por favor revise el script")
            archivo.close()
            exit()
        else: 
            print("Archivo creado y script JSON insertado exitosamente")
            archivo.close()
            

#Variables de entrada    
InputSemana=input("Ingrese semana:")
InputFile=input("Ingrese la ruta y nombre del archivo con extensión json :")
MensajeCommit=("Ingrese mensaje de commit:")
TokenGitHub=input("Ingrese Token:")
NombreRepo=input("Ingrese nombre de Repo:")

#Comprobación de ruta para guardar el archivo
if (os.path.isdir(os.path.dirname(InputFile)) == 0): 
    print("La ruta para guardar el archivo no existe por favor intente de nuevo colocando una ruta existente")
    exit()
#Llamada a la función GetHomeWork creada arriba
GetHomeWork(InputSemana,InputFile)

#Llama a la función creada en el archivo SubirArchivosGitHub.py
SubirGitHub(MensajeCommit,TokenGitHub,InputFile,NombreRepo)
