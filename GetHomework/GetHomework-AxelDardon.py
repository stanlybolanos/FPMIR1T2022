import webbrowser
import requests
import json
from SubirArchivosGitHub import *

#Esta funcion devuelve la tarea de la semana al recibir el numero de semana como parametro
def GetHomework(SemanaN,FilePath):
    #Parte I
    Enalce="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enalce, new=2)
    ##Parte II
    response=requests.get(Enalce).text
    if response == "El Key introducido es invalido o aun no esta disponible":
        print("No hay contenido para esta semana")
        exit()
    try:
        response_info=json.loads(response)
    except:
        print("Hubo un error en la construcción del archivo JSON")
        exit()
    else:
        archivo=open(FilePath, "w")
        json.dump(response_info,archivo,indent=6)
        archivo.close()
def ExisteElDir(QueArchivo):
    ElPathName = os.path.dirname("GetHomework/ArchivosJSON/"+QueArchivo)
    if os.path.exists(ElPathName):
        return True
    else:
        print("No se encontró el path del archivo, no se puede seguir adelante ")
        return False
InputSemana = input("Ingrese semana:")
InputFile = input("Ingrese\ path y nombre de archivo:")
if ExisteElDir(InputFile):
    TokenGithub = input("Ingrese el token: ")
    MensajeCommit = input("Ingrese el mensaje para commit: ")
    NombreRepo = input("Ingrese el nombre para el repositorio: ")
    GetHomework(InputSemana,InputFile)
    SubirGitHub(MensajeCommit,TokenGithub,InputFile,NombreRepo)
else:
    exit()

