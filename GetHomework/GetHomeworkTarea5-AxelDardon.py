import webbrowser
import requests
import json
from SubirArchivosGitHub import *

#Esta funcion devuelve la tarea de la semana al recibir el numero de semana como parametro
def GetHomework(SemanaN,FilePath):
    NoSeContinua = False
    #Parte I
    Enalce="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    #webbrowser.open(Enalce, new=2)
    ##Parte II
    response=requests.get(Enalce).text
    if response == "El Key introducido es invalido o aun no esta disponible":
        print("No hay contenido para esta semana")
        NoSeContinua=True
    else:
        try:
            response_info=json.loads(response)
        except:
            print("Hubo un error en la construcción del archivo JSON")
            NoSeContinua=True
        else:
            ArchivoPath = FilePath
            archivo=open(FilePath, "w")
            json.dump(response_info,archivo,indent=6)
            archivo.close()
    if NoSeContinua:
        return False
    else:
        return True
def ExisteElDir(QueArchivo):
    #ElPathName = os.path.dirname(QueArchivo)
    if os.path.exists(QueArchivo):
        return True
    else:
        print("No se encontró el path para guardar los archivos, no se puede seguir adelante ")
        return False
UsuarioCancelo=False
InputFile = input("Ingrese path para los archivos:")
if ExisteElDir(InputFile):
    #ElPath = os.path.dirname(InputFile)
    InputSemanaNum = 0
    while (InputSemanaNum<1 or InputSemanaNum>10):
        InputSemanaNum = int(input("Ingrese Numero de Semanas (-1 cancela el programa)"))
        if InputSemanaNum<0:
            UsuarioCancelo=True
            break
        if InputSemanaNum<1 or InputSemanaNum>10:
            print("El valor ingresado no es válido, por favor, ingrese un número entre 1 y 10")
    if not UsuarioCancelo:
        TokenGithub = input("Ingrese el token: ")
        MensajeCommit = input("Ingrese el mensaje para commit: ")
        NombreRepo = input("Ingrese el nombre para el repositorio: ")
        x=1
        TerminoAntes=False
        while x<= InputSemanaNum and not TerminoAntes:
            InputSemana = "Semana" + str(x).strip()
            InputSemanaFile = InputSemana + ".json"
            ElFile = InputFile + os.sep + InputSemanaFile
            if GetHomework(InputSemana,ElFile):
                SubirGitHub(MensajeCommit,TokenGithub,ElFile,NombreRepo)
                x+=1
            else:
                TerminoAntes=True
                break
        if TerminoAntes:
            #Hubo error al querer guardar el archivo de la semana x
            print("Se descargaron archivos hasta la semana ",x-1)
        else:
            print("Se lograron descargar todas las semanas exitosamente")
else:
    exit()

