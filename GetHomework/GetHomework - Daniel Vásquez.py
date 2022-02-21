
import webbrowser
import json
import requests
from SubirArchivosGithub import * 
def GetHomework(SemanaN,FilePath):
    enlace ="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}" .format("api", SemanaN)
    webbrowser.open(enlace, new=2)

#parte 2 
    response = requests.get(enlace).text
    response_info = json.loads(response)
    archivo= open(FilePath,"w")
    json.dump(response_info,archivo, indent=6)
    archivo.close()





Inputsemana	= input("ingrese la semana:")
InputFile = input("ingrese  dirección y nombre de archivo")
TokenGiuthub = input("ingrese su token de github")
MensajeCommit = input("ingrese el mensaje")
NombreRepo = input("ingrese el noombre del repositorio")
GetHomework(Inputsemana, InputFile)
