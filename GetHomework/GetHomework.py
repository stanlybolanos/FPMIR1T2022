import webbrowser
import requests
import json
from SubirArchivosGitHub import SubirGitHub, funcion2, funcion3


#Esta funcion devuelve la tarea de la semana al recibir el numero de semana como parametro
def GetHomework(SemanaN,FilePath):
    #Parte I
    Enalce="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enalce, new=2)
    #Parte II
    response=requests.get(Enalce).text
    response_info=json.loads(response)
    archivo=open(FilePath, "w")
    json.dump(response_info,archivo,indent=6)
    archivo.close()


#GetHomework(Num)

InputSemana = input("Ingrese semana:")
InputFile = input("Ingrese path y nombre de archivo:")
GetHomework(InputSemana,InputFile)

Mensaje=input("Ingrese un mensaje para su commit:")
TokenGithub=input("Ingrese su token para autenticarse a Github:")
Repo=input("Ingrese el nombre el repo en github:")

SubirGitHub(MensajeCommit=Mensaje,Token=TokenGithub,Archivo=InputFile,NombreRepo=Repo)
