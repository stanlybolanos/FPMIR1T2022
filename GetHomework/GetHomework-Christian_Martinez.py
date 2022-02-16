## Primera Parte de la tarea
import webbrowser
M=int(input("Ingrese el numero de semana del curso"))
SemanaM=("Semana"+str(M))
homework=("https://fpmir.azurewebsites.net/api/AZFMIR?AZFNUM="+SemanaM)
def GetHomework1(homework):
    webbrowser.open(homework, new=2)
    return homework

GetHomework1(homework)

##Segunda Parte de la tarea
import json
import requests

N=int(input("Ingrese el numero de semana del curso que nos encontramos por favor"))
SemanaN=("Semana"+str(N))
Directorio=input("Ingrese el nombre del directorio")
FilePath=("C:\\"+Directorio+".json")
print(SemanaN)
print(FilePath)

response=requests.get("https://fpmir.azurewebsites.net/api/AZFMIR?AZFNUM"+SemanaN).text
response_info=json.loads(response)
out_file=open(FilePath, "w")
json.dump(response_info, out_file, indent=6)
out_file.close()