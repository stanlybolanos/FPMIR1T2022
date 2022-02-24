from cgitb import text
import webbrowser
import requests
import json
import os
import urllib

def GetHomework(SemanaN,FilePath):
    #Tarea de la primera semana
    Enlace="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    response=requests.get(Enlace).text
    #Validacion para inciso 2
    if response==("El Key introducido es invalido o aun no esta disponible"):
        print("El key introducido es invalido o aun no esta disponible el contenido")
        exit()

        
    else:
        webbrowser.open(Enlace, new=2)
        
        #Tarea de la Segunda semana
        """""
        response=requests.get(Enlace).text
        """""
        response_info=json.loads(response)
        archivo=open(FilePath, "w")
        #Inciso3
        try:
            json.dump(response_info,archivo,indent=6)
        except:
            print("No se logro modificar el archivo json")
        else:
            print("Archivo modificado de manera exitosa")
        finally:
            archivo.close()
InSemana = input("Ingrese la semana del curso:")

PathdeArchivo = input("Ingrese path:")
NombreArchivo = input("Ingrese el nombre del archivo en formato json:")
FileCreado=PathdeArchivo+NombreArchivo
Comprobacion=os.path.exists(PathdeArchivo)
#Validacion para inciso1
if Comprobacion==False:
    print("No se puede continuar debido a que el path no existe")
    exit()
else:
    GetHomework(InSemana,FileCreado)


#Tarea de Semana3
from SubirArchivosGitHub import SubirGitHub

MensajeCommit=input("Ingrese el mensaje que desea para su commit")
TokenGitHub=input("Ingrese el token que obtuvo")
NombreRepo=input("Ingrese el nombre del respositorio que desea el commit")

SubirGitHub(MensajeCommit, TokenGitHub, FileCreado, NombreRepo)
