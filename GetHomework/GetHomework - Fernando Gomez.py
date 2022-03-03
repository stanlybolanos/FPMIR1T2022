from tokenize import Token
from urllib import response
import webbrowser
import requests
import json, os
from SubirArchivosGitHub import SubirGitHub


#Esta funcion devuelve la tarea de la semana al recibir el numero de semana como parametro
def GetHomework(SemanaN,FilePath):
    #Parte I

  for x in range(1,Numero+1):
    SemanaN="Semana"+str(x)
    FilePath=Direccion+"/Semana"+str(x)+".json"

    Enlace="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enlace, new=2)
    #Parte II
    response=requests.get(Enlace).text
    
    if(response=="El key introducido es invalido o aun no esta disponible"):
        print("No hay contenido disponible para esta semana")
        print("Se han grabado correctamente los archivos hasta la semana:",str(x-1))
        exit()

    try:
        response_info=json.loads(response)
        archivo=open(FilePath, "w")
        json.dump(response_info,archivo,indent=6)

    except:
        print("No se puede modificar el archivo")
    
    else:      
        print("Se almaceno exitosamente al archivo:", FilePath)
    
    finally:  
        if(x==SemanaN):
            print("Se han descargado",SemanaN,"Semanas de forma exitosa")
    archivo.close()
            


Numero=int(input("Ingrese el numero de semanas: "))
Direccion=input("Ingrese Path: ")
GetHomework(Numero,Direccion)




"""
if(os.path.isdir(os.path.dirname(Direccion))==False):
    print("El path ingresado:", os.path.dirname(Direccion),"No se encuentra, ingrese un path adecuado.")
else:


#Parte IV
#Verificación del Filepath

Mensaje = input("Ingrese el mensaje del Commit: ")
TokenGithub = input("Ingrese Token para autenticarse a GitHub: ")
Repo = input("Ingrese el Repo de GitHub: ")

SubirGitHub(MensajeCommit=Mensaje, Token=TokenGithub, Archivo=InputFile, NombreRepo=Repo)
"""

