import webbrowser
import requests
import json

def GetHomework(SemanaN,FilePath):
    #Tarea de la Primera Semana
    Enlace="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enlace, new=2)
    #Tarea de la Segunda semana
    response=requests.get(Enlace).text
    response_info=json.loads(response)
    archivo=open(FilePath, "w")
    json.dump(response_info,archivo,indent=6)
    archivo.close()

InSemana = input("Ingrese la semana del curso:")
InFile = input("Ingrese path y el nombre de archivo en formato json:")
GetHomework(InSemana,InFile)

#Tarea de Semana3
from SubirArchivosGitHub import SubirGitHub

MensajeCommit=input("Ingrese el mensaje que desea para su commit")
TokenGitHub=input("Ingrese el token que obtuvo")
NombreRepo=input("Ingrese el nombre del respositorio que desea el commit")

SubirGitHub(MensajeCommit, TokenGitHub, InFile, NombreRepo)
