from cgitb import text
from decimal import ExtendedContext
from urllib import response
import webbrowser
import requests
import json
from SubirArchivosGitHub import SubirGitHub
import os

#Esta funcion devuelve la tarea de la semana al recibir el numero de semana como parametro
def GetHomework(SemanaN,FilePath):
    #Tarea para 24/02/2022, Parte 1
    #Validación de existencia de path
    carpeta=os.path.dirname(InputFile)
    validacion=os.path.exists(carpeta)

    if validacion==False:
        print("No se puede seguir con la ejecución, path/carpeta NO EXISTENTE")
        exit()
    else:
        pass
    #Fin validación existencia de path

    #Parte I
    Enlace="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enlace, new=2)
    
    #Parte II
    response=requests.get(Enlace).text

#Tarea para 24/02/2022, Parte 2
    #Validación de key introducido y verificación de contenido de API
    if response=="El Key introducido es invalido o aun no esta disponible":
        print("No hay contenido para esta semana")
        exit()
    else:
        pass
    #Final de validación de key introducido  
    
#Tarea para 24/02/2022, Parte 3
    #Validación de formato válido JSON   
    try:
        response_info=json.loads(response)
    except:
        print("Este es un mensaje amigable para comentarle que el texto que se intenta obtener no está en formato JSON")
    else:
        archivo=open(FilePath, "w")
        json.dump(response_info,archivo,indent=6)
        archivo.close()
        print("El archivo (.json) fue abierto y cerrado exitosamente")
    finally:
        print("¡Esperamos que vuelva pronto!")
    #Final de validación de formato válido JSON        

InputSemana = input("Ingrese semana:")
InputFile = input("Ingrese \path\ y nombre de archivo:")

GetHomework(InputSemana,InputFile)



#Tarea para 17/02/2022
#Este código es para subir a repositorio el archivo Json 
Mensaje = input("Ingrese mensaje para commit:")
TokenGithub = input("Ingrese token para autentificarse:")
Repo = input("Ingrese nombre de repo en Github:")

#Llamar a la función contenida en script SubirArchivosGitHub.py
SubirGitHub(MensajeCommit=Mensaje,Token=TokenGithub,Archivo=InputFile,NombreRepo=Repo)






