
import webbrowser
import json
import requests
from SubirArchivosGitHub import *
def GetHomework(SemanaN,FilePath):
    response=requests.get(enlace).text
    enlace ="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}" .format("api", SemanaN)
    
    if response==("EL Key introducido es invalido o aun no esta disponible"):
        print("El key introducido es invalido o aun no esta disponible el contenido")
        exit()

    else:
        webbrowser.open(enlace, new=2)
    response_info = json.loads(response)
    archivo= open(FilePath,"w")


    try:
            json.dump(response_info,archivo,indent=6)
    except:
            print("No se logro modificar el archivo json")
    else:
            print("Archivo modificado de manera exitosa")
    finally:
            archivo.close()



    InputSemana	= input("ingrese la semana:")
    InputFile = input("nombre de archivo")
    InputPath = input("Ingrese path de archivo")
    TokenGiuthub = input("ingrese su token de github")
    MensajeCommit = input("ingrese el mensaje")
    NombreRepo = input("ingrese el noombre del repositorio")
    FileCreado = InputPath+InputFile
    comprobacion= os.path.exists(FileCreado)
    if comprobacion == False:
        print("No se puede continuar debido a que el path no existe")

    else:
        SubirGitHub(MensajeCommit,TokenGiuthub,FileCreado,NombreRepo)
        GetHomework(InputSemana, FileCreado)
