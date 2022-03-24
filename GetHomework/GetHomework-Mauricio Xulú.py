import webbrowser
import requests
import json
from SubirArchivosGitHub import SubirGitHub
import os

#Esta funcion devuelve la tarea de la semana al recibir el numero de semana como parametro
def GetHomework(SemanaN,FilePath):
    #Validación de existencia de path
    carpeta=os.path.dirname(InputFile)
    validacion=os.path.exists(carpeta)

    if validacion==False:
        print("No se puede seguir con la ejecución, path/carpeta NO EXISTENTE")
        exit()
    #Fin validación existencia de path

    #Parte I
    Enlace="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)   
    
    #Parte II
    response=requests.get(Enlace).text

#Tarea para 03/03/2022 Parte 2
#Validación de key introducido y verificación de contenido de API  
    if response=="El Key introducido es invalido o aun no esta disponible":
        global ConteoSemanaSinTarea #Se llama a la variable global para indicar que se encontró una semana sin tarea
        ConteoSemanaSinTarea+=1
#Final de validación de key introducido
    
    else:    
        webbrowser.open(Enlace, new=2)

        #Validación de formato válido JSON   
        try:
            response_info=json.loads(response)
        except:
            print("Este es un mensaje amigable para comentarle que el texto que se intenta obtener no está en formato JSON")
        else:
            archivo=open(FilePath, "w")
            json.dump(response_info,archivo,indent=6)
            archivo.close()   
        #Final de validación de formato válido JSON        

InputSemana = int(input("Ingrese las semanas a recopilar:"))
InputFile = input("Ingrese \path de carpeta para almacenar la tareas de las semanas a recopilar:")

#Tarea para 03/03/2022 Parte 1, 2 y 3
#Recopilar las tareas de las semanas ingresadas y guardarlas en path
#Validación para crear break e interrumpir ciclo
#Validación para corroborar si todas las semanas ingresadas se descargaron o si no, cuáles sí fueron descargadas con éxito
ConteoSemanaSinTarea=0
for i in range(1,InputSemana+1):
    GetHomework("Semana"+str(i),InputFile+"Semana"+str(i)+".json")
    if (ConteoSemanaSinTarea==1):   #Validación para crear break si ya se encontró una semana sin tarea, con la ayuda de variable ConteoSemanaSinTarea
        print("Se descargaron archivos hasta la semana",i-1)
        break
else:   #Si el ciclo se terminó por completo significa que todas las semanas ingresadas se descargaron con éxito
    print("¡Se lograron descargar todas las semanas exitosamente!")   


    

"""
#Tarea para 17/02/2022
#Este código es para subir a repositorio el archivo Json 
Mensaje = input("Ingrese mensaje para commit:")
TokenGithub = input("Ingrese token para autentificarse:")
Repo = input("Ingrese nombre de repo en Github:")

#Llamar a la función contenida en script SubirArchivosGitHub.py
SubirGitHub(MensajeCommit=Mensaje,Token=TokenGithub,Archivo=InputFile,NombreRepo=Repo)
"""





