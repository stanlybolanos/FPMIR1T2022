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
   
    if(response.capitalize()=="El key introducido es invalido o aun no esta disponible"):
        print("La semana elegida:",SemanaN,"aun no se encuentra, intente otra semana")
        return False
    try:
        response_info=json.loads(response)
    except:
        print("El contenido de la semana no venia en un formato de JSON valido")
        return False
    else:     
        archivo=open(FilePath, "w")   
        json.dump(response_info,archivo,indent=6)
        print("Se almaceno exitosamente el archivo:",FilePath)
        return True
    finally:
        archivo.close()


#GetHomework(Num)

NumeroSemanas = int(input("Ingrese número de semanas a descargar:"))
InputDirectorio = input("Ingrese el directorio donde se guardaran los archivos:")
InputDirectorio = InputDirectorio.strip("\\")
ResultadoGetHomework = False
#c:\Tareas\
#c:\Tareas+\+Semana1.json
if(not(os.path.isdir(InputDirectorio))):
    print("El path ingresado:",os.path.dirname(InputDirectorio),"no se encuentra, porfavor ingrese un path valido")
else:
    for i in range(1,NumeroSemanas+1):
        ResultadoGetHomework=GetHomework("Semana{0}".format(i),InputDirectorio+"\\"+"Semana{0}".format(i))
        if ResultadoGetHomework==False: 
            print("Se logro descargar hasta la semana numero:",i-1)
            break
    else:
        print("Todas las semanas se lograron almacenar exitosamente")
#Semana+str(i)
"""
Mensaje=input("Ingrese un mensaje para su commit:")
TokenGithub=input("Ingrese su token para autenticarse a Github:")
Repo=input("Ingrese el nombre el repo en github:")

SubirGitHub(MensajeCommit=Mensaje,Token=TokenGithub,Archivo=InputFile,NombreRepo=Repo)
"""
