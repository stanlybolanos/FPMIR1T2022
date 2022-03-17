import os
from time import sleep
import urllib.request
import re
import webbrowser
from pytube import YouTube
import Funciones
def MostrarVideos():
    # Esta subrutina solicita el número o números (separados por comas), de los videos que el usuario desea
    # observar en el navegador, y procede a desplegarlos; si el número o números ingresados no corresponden
    # con un video válido, muestra un mensaje de error
    QueVideos=input("Ingrese el número de video que desea observar, o la lista de videos separado por comas: ")
    EsLista = False
    ElItem = 0
    ElError = ""
    if QueVideos.find(",")>=0:
        #Tiene comas
        LaLista=QueVideos.split(",")
        j=0
        for xx in LaLista:
            try:
                UnItem=int(xx.strip())
            except:
                ElError = ElError + "El " + xx.strip() + " no es un valor válido, "
            else:
                if UnItem>=1 and UnItem<=Funciones.I+1:
                    try:
                        webbrowser.open(Funciones.V[UnItem-1], new=2)
                    except:
                        print("No fue posible mostrar el video {0}".format(UnItem))
    else:
        #no tiene comas
        try:
            UnItem = int(QueVideos)
        except:
            UnItem=0
        if UnItem>=1 and UnItem<=Funciones.I+1:
            try:
                webbrowser.open(Funciones.V[UnItem-1], new=2)
            except:
                print("No fue posible mostrar el video {0}".format(UnItem))


def BuscarVideos():
    # Esta subrutina se utiliza para buscar videos en youtube, se solicita al usuario el texto de búsqueda
    # luego se realiza la búsqueda del texto en el sitio web de youtube utilizando la funcion request de la
    # utilería urllib; esta utilería devuelve un listado de los videos encontrados a traves de la utilería
    # re.findall; posteriormente solicita la cantidad de resultados que se requieren almacenar
    # según requerimiento, solo puede solicitar entre 1 y 5 resultados.
    # Las direcciones de los videos obtenidos se almacenan en la lista V y el contador I registra 
    # la cantidad de videos menos uno.  Finalmente se procede a mostrar los videos utilizando la subrutina
    # MostrarVideos
    CantidadValida=False
    Busqueda = input("Ingrese texto de búsqueda:")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + Busqueda)
    Video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    Cuantos,CantidadValida=Funciones.IngreseNumero("Ingrese Resultados:",1,5)
    if CantidadValida:
        n=0
        for x in Video_ids:
            n+=1
            ElVideo="https://www.youtube.com/watch?v="+x
            Funciones.V.append(ElVideo)
            #print(ElVideo)
            try:
               yt=YouTube(ElVideo)
            except Exception as e:
               print (e)
            else:
                print("Resultado de video #{0} con título {1} - {2} ".format(n,yt.title,ElVideo))
                Funciones.I += 1
                if n==Cuantos:
                    break
        MostrarVideos()
    else:
        print("Por favor, ingrese un número entre 1 y 5")
        sleep(5)