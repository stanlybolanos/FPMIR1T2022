import webbrowser
import requests
import json
from SubirArchivosGitHub import SubirGitHub

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

InputSemana = input("Ingrese semana:")
InputFile = input("Ingrese\ path y nombre de archivo:")

Mensaje = input("Ingrese mensaje para commit:")
TokenGithub = input("Ingrese token para autentificarse:")
Repo = input("Ingrese nombre de repo en Github:")

GetHomework(InputSemana,InputFile)

#Tarea para 17/02/2022
#Llamar a la función contenida en script SubirArchivosGitHub.py
SubirGitHub(MensajeCommit=Mensaje,Token=TokenGithub,Archivo=InputFile,NombreRepo=Repo)




