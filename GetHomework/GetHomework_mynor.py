from importlib import import_module
import webbrowser
import requests
import json
import os
from  SubirArchivosGitHub  import SubirGitHub

#Esta funcion devuelve la tarea de la semana al recibir el numero de semana como parametro
def GetHomework(SemanaN,FilePath):
    #Parte I
    Enalce="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enalce, new=2)
    #Parte II
    response=requests.get(Enalce).text
    response_info=json.loads(response)
    # validacion si existe carpeta continua si no existe se sale. 
    if os.path.exists(FilePath)==False:
       exit()

    archivo=open(FilePath, "w")
    json.dump(response_info,archivo,indent=6)
    archivo.close()

InputSemana = input("Ingrese semana:")
InputFile = input("Ingrese\ path y nombre de archivo:")
GetHomework(InputSemana,InputFile)
v_Mensaje = input("ingrese mensaje : ")
v_token = "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"
v_archivo = input("nombre archivo : ")
v_repo = input("ingrese Nombre repositorio")

SubirGitHub(v_Mensaje,v_token ,v_archivo ,v_repo) 
