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
    json.dump(response_info,archivo,indent=6)
    archivo.close()

InputSemana = input("Ingrese semana: ")
DireccionAPI = requests.get("https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",InputSemana))

if (DireccionAPI._content=="El Key introducido es invalido o aun no esta disponible"):
    print(DireccionAPI._content)
    print("No hay contenido para esta semana")
    exit()

InputFile = input("Ingrese\ path y nombre de archivo: ")
if os.path.exists(InputFile):
   print("El path si existe. ")
else:
   print("El path no existe, se procederá a salir.")
   exit()


GetHomework(InputSemana,InputFile)


import requests
import json
response_API = requests.get(Enlace).text
print(response_API._content)



Mensaje = input("Ingrese el mensaje del Commit: ")
TokenGithub = input("Ingrese Token para autenticarse a GitHub: ")
Repo = input("Ingrese el Repo de GitHub: ")

SubirGitHub(MensajeCommit=Mensaje, Token=TokenGithub, Archivo=InputFile, NombreRepo=Repo)

