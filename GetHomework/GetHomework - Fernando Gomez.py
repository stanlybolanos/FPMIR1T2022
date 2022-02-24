from tokenize import Token
from urllib import response
import webbrowser
import requests
import json, os
from SubirArchivosGitHub import SubirGitHub


#Esta funcion devuelve la tarea de la semana al recibir el numero de semana como parametro
def GetHomework(SemanaN,FilePath):
    #Parte I
    Enlace="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enlace, new=2)
    #Parte II
    response=requests.get(Enlace).text
    response_info=json.loads(response)
    archivo=open(FilePath, "w")
    try:
        json.dump(response_info,archivo,indent=6)
    except:
        print("Ocurrió un problema al crear el archivo JSON")
    else:
        print("El archivio ha sido creado exitosamente")
    finally:
        archivo.close()

InputSemana = input("Ingrese semana: ")
#Verificación del API para el contenido de la semana.
DireccionAPI = requests.get("https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",InputSemana))
if (DireccionAPI.text=="El Key introducido es invalido o aun no esta disponible"):
    print("No hay contenido para esta semana")
    exit()


InputFile = input("Ingrese\ path y nombre de archivo: ")
#Verificación de la extensión .json.
root, extension = os.path.splitext(InputFile)
if (extension!='.json'):
    print("La extensión JSON es invalida.")
    exit()


#Verificación del Filepath
if os.path.exists(InputFile):
   print("El path si existe. ")
else:
   print("El path no existe, se procederá a salir.")
   exit()


GetHomework(InputSemana,InputFile)

Mensaje = input("Ingrese el mensaje del Commit: ")
TokenGithub = input("Ingrese Token para autenticarse a GitHub: ")
Repo = input("Ingrese el Repo de GitHub: ")

SubirGitHub(MensajeCommit=Mensaje, Token=TokenGithub, Archivo=InputFile, NombreRepo=Repo)

