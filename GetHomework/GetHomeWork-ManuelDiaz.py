#Importaciones
import webbrowser
import requests
import json
    #Importación de la función creada en el archivo SubirArchivosGitHub
from SubirArchivosGitHub import *
#Esta función devuelve la tarea de la semana al recibir el numero de seman como parámetro
def GetHomeWork(SemanaN,FilePath):
    #Parte 1
    Enlace="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enlace, new=2)
    #Parte 2
    response=requests.get(Enlace).text
    response_info=json.loads(response)
    archivo=open(FilePath,"w")
    json.dump(response_info,archivo,indent=6)
    archivo.close()
    
InputSemana=input("Ingrese semana:")
InputFile=input("Ingrese path y nombre del archivo:")
MensajeCommit=("Ingrese mensaje de commit:")
TokenGitHub=input("Ingrese Token:")
NombreRepo=input("Ingrese nombre de Repo:")

GetHomeWork(InputSemana,InputFile)
#Llamada a la función creada en el archivo SubirArchivosGitHub.py
SubirGitHub(MensajeCommit,TokenGitHub,InputFile,NombreRepo)
