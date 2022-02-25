import webbrowser
import requests
import json
from SubirArchivosGitHub import SubirGitHub, funcion2, funcion3
import os


#Esta funcion devuelve la tarea de la semana al recibir el numero de semana como parametro
def GetHomework(SemanaN,FilePath):
    #Parte I
    Enalce="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enalce, new=2)
    #Parte II
    response=requests.get(Enalce).text
    archivo=open(FilePath, "w")
    if(response.capitalize()=="El key introducido es invalido o aun no esta disponible"):
        print("La semana elegida:",SemanaN,"aun no se encuentra, intente otra semana")
        exit()
    try:
        response_info=json.loads(response)
        json.dump(response_info,archivo,indent=6)
    except:
        print("El contenido de la semana no venia en un formato de JSON valido")
    else:        
        
        print("Se almaceno exitosamente el archivo:",FilePath)
    finally:
        archivo.close()


#GetHomework(Num)

InputSemana = input("Ingrese semana:")
InputFile = input("Ingrese path y nombre de archivo:")
if(not(os.path.isdir(os.path.dirname(InputFile)))):
    print("El path ingresado:",os.path.dirname(InputFile),"no se encuentra, porfavor ingrese un path valido")
else:
    GetHomework(InputSemana,InputFile)

"""
Mensaje=input("Ingrese un mensaje para su commit:")
TokenGithub=input("Ingrese su token para autenticarse a Github:")
Repo=input("Ingrese el nombre el repo en github:")

SubirGitHub(MensajeCommit=Mensaje,Token=TokenGithub,Archivo=InputFile,NombreRepo=Repo)
"""
