import os
from time import sleep
import webbrowser
from pytube import YouTube
import Funciones
def DescargarVideos():
    # Esta subrutina se utiliza para descargar el o los videos que el usuario solicite, las direcciones de los videos
    # se obtienen de la lista V, la cual fue llenada en la opción 1 del programa; estos videos se almacenan en un directorio 
    # indicado por el usuario; los videos se nombran como Video#.3gpp (donde # representa el número de video seleccionado)
    # .3gpp es la extensión por defecto para los videos descargados de youtube
    # una vez descargado el video, se consulta al usuario si desea visualizar el video descargado
    # si el usuario responde afirmativamente, se procede a mostrar el video utilizando el programa wmplayer
    # a traves de una ventana de shell (por medio de la funcion os.system)
    QueVideos=input("Ingrese el número de video que desea descargar, o la lista de videos separado por comas: ")
    QueDirectorio=input("Por favor, ingrese el directorio donde desea almacenar " + ("los videos" if QueVideos.find(",")>=0 else "el video")+ ": ")
    if not os.path.isdir(QueDirectorio):
        print("El directorio seleccionado no existe, por favor, verifique")
        sleep(5)
    else:
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
                            #ya tiene seleccionado el video en V[UnItem-1]
                            yt=YouTube(Funciones.V[UnItem-1])
                            print("Descargando archivo ",yt.title)
                            yt.streams.first().download(QueDirectorio,"Video"+str(UnItem)+".3gpp")
                            print("Archivo: ",yt.title,"descargado")
                            QuiereVerlo=input("Si desea ver el video recien descargado (s/n): ")
                            if QuiereVerlo.strip() == "S" or QuiereVerlo.strip() == "s":
                                print("Reproduciendo Video")
                                os.system("start wmplayer "+chr(34) + QueDirectorio + os.sep + "Video"+str(UnItem)+".3gpp"+chr(34))
                        except:
                            print("No fue posible descargar el video {0}".format(UnItem))
        else:
            #no tiene comas
            try:
                UnItem = int(QueVideos)
            except:
                UnItem=0
            if UnItem>=1 and UnItem<=Funciones.I+1:
                try:
                    yt=YouTube(Funciones.V[UnItem-1])
                    print("Descargando archivo ",yt.title)
                    yt.streams.first().download(QueDirectorio,"Video"+str(UnItem)+".3gpp")
                    print("Archivo: ",yt.title,"descargado")
                    QuiereVerlo=input("Si desea ver el video recien descargado (s/n)")
                    if QuiereVerlo.strip() == "S" or QuiereVerlo.strip() == "s":
                        print ("Reproduciendo")
                        os.system("start wmplayer "+chr(34) + QueDirectorio + os.sep + "Video"+str(UnItem)+".3gpp"+chr(34))
                except:
                    print("No fue posible mostrar el video {0}".format(UnItem))
