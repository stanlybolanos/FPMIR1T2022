import os
from time import sleep
from pytube import YouTube
import cls_funciones
import urllib.request
import re
import webbrowser
class Video:
    DireccionVideo="C:\videos"
    def __init__(self,p_LinkVideo):
        self.LinkVideo=p_LinkVideo
   
    @classmethod
    def CambioDirectorio(cls,NuevoDirectorio):
        Video.DireccionVideo=NuevoDirectorio
    @staticmethod
    def MostrarVideo(QueNumVideo):
        try:
            UnItem = QueNumVideo
        except:
            UnItem=0
        if UnItem>=1:
            try:
                webbrowser.open(cls_funciones.V[UnItem-1].LinkVideo, new=2)
            except:
                print("No fue posible mostrar el video {0}".format(UnItem)) 
    @staticmethod
    def DescargarVideo(CualVideo):
        PudoDescargarlo=False
        if not os.path.isdir(Video.DireccionVideo):
            print("El directorio seleccionado no existe, por favor, verifique")
            sleep(5)
        else:
            try:
                UnItem = int(CualVideo)
            except:
                UnItem=0
            if UnItem>=1:
                try:
                    yt=YouTube(cls_funciones.V[UnItem-1].LinkVideo)
                    #Video.__TituloVideo=yt.title
                    print("Descargando archivo ",yt.title)
                    yt.streams.first().download(Video.DireccionVideo,"Video"+str(UnItem)+".3gpp")
                    print("Archivo: ",yt.title,"descargado")
                    PudoDescargarlo=True
                    QuiereVerlo=input("Si desea ver el video recien descargado (s/n)")
                    if QuiereVerlo.strip() == "S" or QuiereVerlo.strip() == "s":
                        print ("Reproduciendo")
                        os.system("start wmplayer "+chr(34) + Video.DireccionVideo + os.sep + "Video"+str(UnItem)+".3gpp"+chr(34))
                except:
                    print("No fue posible mostrar el video {0}".format(UnItem))        
        return PudoDescargarlo


class Busqueda:
    TextoABuscar=""
    NumeroResultados=0
    @classmethod
    def CambioTextoABuscar(cls,NuevoTextoABuscar):
        Busqueda.TextoABuscar=NuevoTextoABuscar
    @classmethod
    def CambioNumeroResultados(cls,NuevoNumeroResultados):
        Busqueda.NumeroResultados=NuevoNumeroResultados
    @staticmethod
    def HacerBusqueda(): 
        LoLogro=False
        if cls_funciones.I<0:
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + Busqueda.TextoABuscar)
            Video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            n=0
            for x in Video_ids:
                n+=1
                ElVideo="https://www.youtube.com/watch?v="+x
                cls_funciones.V.append(Video(ElVideo))
                #print(ElVideo)
                try:
                   yt=YouTube(ElVideo)
                except Exception as e:
                   print (e)
                else:
                    print("Resultado de video #{0} con título {1} - {2} ".format(n,yt.title,ElVideo))
                    cls_funciones.I += 1
                    LoLogro=True
                    xy=input("Desea mostrarlo en el navegador (S/N)")
                    if xy=="S" or xy=="s":
                        cls_funciones.V[n-1].MostrarVideo(n)

                    if n==Busqueda.NumeroResultados:
                        break
        else:
            xy=input("Ya tiene una lista cargada, desea borrala (S/N)?")
            if xy=="S" or xy=="s":
                # Limpie la lista y coloque I en menos uno para indicar que no hay lista disponible
                cls_funciones.V.clear()
                cls_funciones.I=-1
        return LoLogro

def BusqueLosVideos():
    QueBusca = input("Ingrese texto de búsqueda:")
    if QueBusca.strip() > "":
        Cuantos,CantidadValida=cls_funciones.IngreseNumero("Ingrese Resultados:",1,5)
        if CantidadValida:
            Busqueda.CambioTextoABuscar(QueBusca)
            Busqueda.CambioNumeroResultados(Cuantos)
            if Busqueda.HacerBusqueda():
                print("Se encontraron los videos buscados")
            
def  MuestreLosVideos():
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
                if UnItem>=1 and UnItem<=cls_funciones.I+1:
                    if cls_funciones.V[UnItem-1].MostrarVideo(UnItem):
                        print("El video {0} fue mostrado".format(UnItem))
    else:
        #no tiene comas
        try:
            UnItem = int(QueVideos)
        except:
            UnItem=0
        if UnItem>=1 and UnItem<=cls_funciones.I+1:
            if cls_funciones.V[UnItem-1].MostrarVideo(UnItem):
                print("El video {0} fue mostrado".format(UnItem))

def DescargueLosVideos():
    if cls_funciones.I>=0:
        QueVideos=input("Ingrese el número de video que desea descargar, o la lista de videos separado por comas: ")
        QueDirectorio=input("Por favor, ingrese el directorio donde desea almacenar " + ("los videos" if QueVideos.find(",")>=0 else "el video")+ ": ")
        if not os.path.isdir(QueDirectorio):
            print("El directorio seleccionado no existe, por favor, verifique")
            sleep(5)
        else:
            Video.CambioDirectorio(QueDirectorio)
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
                        if UnItem>=1 and UnItem<=cls_funciones.I+1:
                            if cls_funciones.V[UnItem-1].DescargarVideo(UnItem):
                                print("El Video {0} fue descargado".format(UnItem))
            else:
                #no tiene comas
                try:
                    UnItem = int(QueVideos)
                except:
                    UnItem=0
                if UnItem>=1 and UnItem<=cls_funciones.I+1:
                    if cls_funciones.V[UnItem-1].DescargarVideo(UnItem):
                        print("El Video {0} fue descargado".format(UnItem))

#Inicio del programa principal
SeSale = False
UnaOpcion=0
while not SeSale:
    # Limpiar pantalla
    cls_funciones.CS()
    # Muestra el menú principal
    print("Menú Principal")
    print("")
    print("1) Búsqueda de Video")
    print("2) Descarga de Video")
    print("3) Comprimir y Descomprimir Videos")
    print("4) Selección de Frames de Video")
    print("5) Identificar Contenido en Video")
    print("6) Reporte de Contenido")
    print("7) Salida")
    print("")
    OpcionValida=False
    # Se solicita el ingreso de una opción válida entre 1 y 7
    UnaOpcion,OpcionValida=cls_funciones.IngreseNumero("Ingrese una Opción:",1,7)
    if not OpcionValida: # La opción seleccionada no es válida
        print("La opción seleccionada no es válida, por favor, revise su selección")
        sleep(5)
    elif UnaOpcion==7: # Seleccionó la opcion 7: Salir del programa
        SeSale=True
    elif UnaOpcion==1: #Selecciono la opción 1: Búsqueda de videos
        if cls_funciones.I>=0:
            # Existen datos en la lista de videos
            xy=input("Ya tiene una lista cargada, desea borrala (S/N)?")
            if xy=="S" or xy=="s":
                # Limpie la lista y coloque I en menos uno para indicar que no hay lista disponible
                cls_funciones.V.clear()
                cls_funciones.I=-1
                # Haga la búsqueda de videos como si fuera la primera vez
                BusqueLosVideos()
            else:
                # Muestre los videos que el usuario seleccione de la lista existente
                MuestreLosVideos()
        else:
            # Busque videos porque la lista esta vacía
            BusqueLosVideos()
    elif UnaOpcion==2: # Seleccionó la opción 2: Descarga de Video
        if cls_funciones.I>=0:
            # Existen datos en la lista
            # Descargue los videos que seleccione el usuario
            DescargueLosVideos()
        else:
            # La lista de videos esta vacía
            print("Aún no ha almacenado videos, por favor, seleccione la opción 1 primero")
            sleep(5)
print("El usuario salio del programa")

