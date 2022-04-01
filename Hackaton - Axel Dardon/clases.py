import os
from time import sleep
#from typing_extensions import Self
from pytube import YouTube
import cls_funciones
import urllib.request
import re
import webbrowser
import errno
import zipfile
import cv2
class Video:
    DireccionVideo="C:\videos"
    __Titulo=""
    def __init__(self,p_NumeroVideo,p_LinkVideo):
        self.NumeroVideo=p_NumeroVideo
        self.LinkVideo=p_LinkVideo

    def PongaTitulo(self,ElTitulo):
        self.__Titulo=ElTitulo

       
    @classmethod
    def CambioDirectorio(cls,NuevoDirectorio):
        Video.DireccionVideo=NuevoDirectorio
 
    def MostrarVideo(self):
        try:
            #webbrowser.open(cls_funciones.V[UnItem-1].LinkVideo, new=2)
            webbrowser.open(self.LinkVideo, new=2)
        except:
            print("No fue posible mostrar el video {0}".format(self.NumeroVideo)) 
    
    def DescargarVideo(self,EnDonde):
        PudoDescargarlo=False
        if EnDonde=="":
           EnDonde=self.DireccionVideo
        if not os.path.isdir(EnDonde):
            print("El directorio seleccionado no existe, por favor, verifique")
            sleep(5)
        else:
            try:
                yt=YouTube(self.LinkVideo)
                SiSale=False
                Aborto=False
                ElTag=[]
                LaExte=[]                
                ElVideoSeleccionado=""
                LaSeleccion=0
                NumeroValido=False
                while not SiSale:
                    cls_funciones.CS()
                    print("Mostrando los streams disponibles en ",yt.title)
                    print("")
                    l=0
                    ElTag.clear
                    LaExte.clear
                    try:
                        for stream in yt.streams.all():
                            ElTag.append(stream.itag)
                            LaExte.append(stream.subtype)
                            l+=1
                            print("{4}) TAG:{0}, Formato {1}, Resolución {2}, Cuadros Por Segundo: {5}, Extension: {3}".format(stream.itag,stream.mime_type,stream.resolution,stream.subtype,l,stream.fps))
                    except:
                        print("")
                    LaSeleccion,NumeroValido = cls_funciones.IngreseNumero("Por favor, ingrese el número de stream que desea descargar (0 para cancelar)",0,l)
                    if NumeroValido:
                        if LaSeleccion==0:
                            SiSale=True
                            Aborto=True
                        else:
                            print("Se inicia la descarga de ",yt.title," por favor, espere...")
                            stream = yt.streams.get_by_itag(ElTag[LaSeleccion-1])
                            ElVideoSeleccionado="Video"+str(self.NumeroVideo)+"."+LaExte[LaSeleccion-1]
                            stream.download(EnDonde,ElVideoSeleccionado)
                            print("Archivo: ",yt.title,"descargado como Video"+str(self.NumeroVideo)+"."+LaExte[LaSeleccion-1])
                            SiSale=True
                    
                #yt.streams.first().download(EnDonde,"Video"+str(self.NumeroVideo)+".3gpp")
                if not Aborto:
                    PudoDescargarlo=True
                    QuiereVerlo=input("Si desea ver el video recien descargado (s/n)")
                    if QuiereVerlo.strip() == "S" or QuiereVerlo.strip() == "s":
                        print ("Reproduciendo")
                        os.system("start wmplayer "+chr(34) + EnDonde + os.sep + ElVideoSeleccionado +chr(34))
            except:
                print("Existieron errores al tratar de descargar el video {0}".format(self.NumeroVideo))     
                sleep(5)   
        return PudoDescargarlo

class Busqueda:
    TextoABuscar=""
    NumeroResultados=0
    @staticmethod
    def CambioTextoABuscar(NuevoTextoABuscar):
        Busqueda.TextoABuscar=NuevoTextoABuscar
    @staticmethod
    def CambioNumeroResultados(NuevoNumeroResultados):
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
                cls_funciones.V.append(Video(n,ElVideo))
                #print(ElVideo)
                try:
                   yt=YouTube(ElVideo)
                   cls_funciones.V[n-1].PongaTitulo(yt.title)
                except Exception as e:
                   print (e)
                else:

                    print("Resultado de video #{0} con título {1} - {2} ".format(n,yt.title,ElVideo))
                    cls_funciones.I += 1
                    LoLogro=True
                    xy=input("Desea mostrarlo en el navegador (S/N)")
                    if xy=="S" or xy=="s":
                        cls_funciones.V[n-1].MostrarVideo()

                    if n==Busqueda.NumeroResultados:
                        break
        else:
            xy=input("Ya tiene una lista cargada, desea borrala (S/N)?")
            if xy=="S" or xy=="s":
                # Limpie la lista y coloque I en menos uno para indicar que no hay lista disponible
                cls_funciones.V.clear()
                cls_funciones.I=-1
        return LoLogro
def CreeDirectorioDeTrabajo(UnDirectorio):
    SiLoPudoCrear=False
    Continue=True
    UnDirectorio.strip(os.sep)
    if UnDirectorio=="":
        print("El directorio {0} No Existe".format(UnDirectorio))
        sleep(5)
        Continue=False
    elif not os.path.isdir(UnDirectorio):
        print("El directorio {0} No Existe".format(UnDirectorio))
        sleep(5)
        Continue=False
    else:    
        if not os.path.isdir(os.path.join(UnDirectorio, "Frames")):
            try:
                os.mkdir(os.path.join(UnDirectorio, "Frames"))
            except OSError as e:
                print("No fue postible crear el sub-directorio: Fames debido a {0}, se cancela asignación de directorio de trabajo".format(e.strerror(e.errno)))
                Continue=False
                #if e.errno != errno.EEXIST:
                    #raise
                    #Hubo un error
        if Continue:
            if not os.path.isdir(os.path.join(UnDirectorio, "VideosComprimidos")):
                try:
                    os.mkdir(os.path.join(UnDirectorio, "VideosComprimidos"))
                except OSError as e:
                    print("No fue postible crear el sub-directorio: VideosComprimidos debido a {0}, se cancela asignación de directorio de trabajo".format(e.strerror(e.errno)))
                    Continue=False
        if Continue:
            if not os.path.isdir(os.path.join(UnDirectorio, "VideosDescargados")):
                try:
                    os.mkdir(os.path.join(UnDirectorio, "VideosDescargados"))
                except OSError as e:
                    print("No fue postible crear el sub-directorio: VideosDescargados debido a {0}, se cancela asignación de directorio de trabajo".format(e.strerror(e.errno)))
                    Continue=False
        if Continue:
            if not os.path.isdir(os.path.join(UnDirectorio, "VideosSinCompresion")):
                try:
                    os.mkdir(os.path.join(UnDirectorio, "VideosSinCompresion"))
                except OSError as e:
                    print("No fue postible crear el sub-directorio: VideosSinCompresion debido a {0}, se cancela asignación de directorio de trabajo".format(e.strerror(e.errno)))
                    Continue=False
                    SiLoPudoCrear=True
        if Continue:
            try:
                os.chdir(UnDirectorio)
            except OSError as e:
                print("No fue postible crear el sub-directorio: VideosSinCompresion debido a {0}, se cancela asignación de directorio de trabajo".format(e.strerror(e.errno)))
            else:
                cls_funciones.DirectorioRelativo=UnDirectorio
                SiLoPudoCrear=True
    return SiLoPudoCrear

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
                    cls_funciones.V[UnItem-1].MostrarVideo()

    else:
        #no tiene comas
        try:
            UnItem = int(QueVideos)
        except:
            UnItem=0
        if UnItem>=1 and UnItem<=cls_funciones.I+1:
            cls_funciones.V[UnItem-1].MostrarVideo()


def DescargueLosVideos(EnDonde):
    if cls_funciones.I>=0:
        QueVideos=input("Ingrese el número de video que desea descargar, o la lista de videos separado por comas: ")
        #QueDirectorio=input("Por favor, ingrese el directorio donde desea almacenar " + ("los videos" if QueVideos.find(",")>=0 else "el video")+ ": ")
        if EnDonde=="":
            EnDonde =os.path.join(cls_funciones.DirectorioRelativo,"VideosDescargados")
        if not os.path.isdir(EnDonde):
            print("El directorio seleccionado para almacenar videos ya no existe, por favor, verifique")
            sleep(5)
        else:
            QueDirectorio=EnDonde
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
                            if cls_funciones.V[UnItem-1].DescargarVideo(QueDirectorio):
                                print("El Video {0} fue descargado".format(UnItem))
            else:
                #no tiene comas
                try:
                    UnItem = int(QueVideos)
                except:
                    UnItem=0
                if UnItem>=1 and UnItem<=cls_funciones.I+1:
                    if cls_funciones.V[UnItem-1].DescargarVideo(QueDirectorio):
                        print("El Video {0} fue descargado".format(UnItem))

def ManejoDePath():
    HayQuePreguntar=False
    if cls_funciones.DirectorioRelativo=="":
        HayQuePreguntar=True
    else:
        NuevoDirectorio=input("Ya ha sido asignado el directorio de trabajo: {0} desea reasignarlo (S/N): ".format(cls_funciones.DirectorioRelativo))
        NuevoDirectorio=NuevoDirectorio.strip()
        if NuevoDirectorio=="S" or NuevoDirectorio=="s":
            cls_funciones.DirectorioRelativo=""
            HayQuePreguntar=True
    if HayQuePreguntar:
        #no ha definido el directorio relativo
        UnDirectorio=input("Por favor ingrese un directorio de trabajo (si lo deja en blanco, se asignará {0}):".format(os.getcwd()))
        UnDirectorio = UnDirectorio.strip()
        if UnDirectorio=="":
            UnDirectorio=os.getcwd()
        if not os.path.isdir(UnDirectorio):
            print("El directorio {0} No Existe, no fue posible asignar el directorio de trabajo".format(UnDirectorio))
            sleep(5)
        else:
            if CreeDirectorioDeTrabajo(UnDirectorio):
                print("Directorio de Trabajo: {0} Creado Exitosamente!!!".format(UnDirectorio))
            else:
                print("No fue posible crear el directorio {0} ".format(UnDirectorio))
                sleep(5)

def BuscarFrames():
    cls_funciones.CS()
    UnDirecto=input("Seleccione Video para extraer frames (ingrese el path relativo, siempre se adicionará al directorio de trabajo): ")
    LaAdress = os.path.join(cls_funciones.DirectorioRelativo, UnDirecto)
    if os.path.isfile(LaAdress):
        print("El video {0} fue encontrado!".format(LaAdress))
        #No es necesario hacer la validación del directorio frames, porque ya existe, pero si vamos a crear el directorio del archivo
        NombreYExtension=os.path.basename(LaAdress).split(".")
        Continue=True
        DirectorioDestino=os.path.join(cls_funciones.DirectorioRelativo, "Frames",NombreYExtension[0])
        if not os.path.isdir(DirectorioDestino):
            try:
                os.mkdir(DirectorioDestino)
            except OSError as e:
                print("No fue postible crear el sub-directorio: {1} debido a {0}, se cancela el proceso".format(e.strerror(e.errno),DirectorioDestino))
                Continue=False
        if Continue:
            print("Fue creado el directorio {0}".format(DirectorioDestino))
            QueFrame=input("Por favor, ingrese el número de frame que desea descargar (si desea varios, coloquelos separados por comas) o 0 para descargar todos: ")
            FI=[]
            j=0
            if QueFrame.find(",")>=0:
                #Tiene comas
                LaLista=QueFrame.split(",")
                for xx in LaLista:
                    try:
                        UnItem=int(xx.strip())
                    except:
                        ElError = ElError + "El " + xx.strip() + " no es un valor válido, "
                    else:
                        if UnItem>=1:
                            FI.append(UnItem)
                            j+=1
            else:
                #No tiene comas
                try:
                    UnItem = int(QueFrame)
                except:
                    UnItem=0
                else:
                    if UnItem==0:
                        #Quiere todos
                        j=-1
                    else:
                        #Quiere uno en particular
                        FI.append(UnItem)
                        j=1
            if j==0:
                #No hay
                print("No se seleccionaron frames para descargar")
            else:
                Continue=False
                try:
                    vidcap=cv2.VideoCapture(LaAdress)
                except:
                    print("Se encontraron problemas con el video, se cancela la descarga")
                    sleep(5)
                else:
                    Continue=True
                if Continue:
                    if j<0:
                        success,imagen=vidcap.read()
                        count=0
                        while success:
                            count+=1
                            ElNombre="Frame"+str(count)+".jpg"
                            try:
                                cv2.imwrite(os.path.join(DirectorioDestino, ElNombre),imagen) #salvar imagen
                            except:
                                print ("Existió un error al tratar de guardar el frame {0}".format(count))
                                sleep(5)
                            success,imagen=vidcap.read()
                    else:
                        for ll in FI:
                            vidcap.set(1,ll)
                            success,imagen=vidcap.read()
                            if success:
                                ElNombre="Frame"+str(ll)+".jpg"
                                try:
                                    cv2.imwrite(os.path.join(DirectorioDestino, ElNombre),imagen) #salvar imagen
                                except:
                                    print ("Existió un error al tratar de guardar el frame {0}".format(ll))
                                    sleep(5)
    else:
        print("El archivo seleccionado no es válido")
        sleep(5)
def MuestreArchivos(QueDirectorio):
    Direcciones=[]
    try:
        for Raiz,Directorios,Archivos in os.walk(QueDirectorio):
            for Archivo in Archivos:
                UnaDireccion=os.path.join(Raiz,Archivo)
                Direcciones.append(UnaDireccion)
    except:
        print("Existió un error")
    return Direcciones
def ComprimaVideos():
    #Debe permitir al usuario elegir que videos va a comprimir, puede utilizar videosdescargados o seleccionar otra carpeta
    DirectorioBase=os.path.join(cls_funciones.DirectorioRelativo, "VideosDescargados")
    LosArchivos=MuestreArchivos(DirectorioBase)
    if len(LosArchivos)<=0:
        #No hay archivos
        print("No hemos encontrado archivos que comprimir en el directorio por default, ")
        UnDirectorio=input("Ingrese el directorio donde se encuentran los archivos que desea comprimir: ")
        UnDirectorio.strip(os.sep)
        EncontroDirectorio=False
        if UnDirectorio=="":
            print("El directorio {0} No Existe".format(UnDirectorio))
            sleep(5)
        elif not os.path.isdir(UnDirectorio):
            print("El directorio {0} No Existe".format(UnDirectorio))
            sleep(5)
        else:
            LosArchivos=MuestreArchivos(UnDirectorio)
            if len(LosArchivos)>0:
                DirectorioBase=UnDirectorio
                EncontroDirectorio=True
    else:
        EncontroDirectorio=True

    if EncontroDirectorio:
        k=0
        print("Se encontraron los siguientes archivos: ")
        UA=[]
        for UnArchivo in LosArchivos:
            UA.append(UnArchivo)
            k+=1
            print("{0}) {1}".format(k,UnArchivo))
        print("")
        ElError=""
        UnaRespuesta=input("Por favor, seleccione uno (#) o varios (# separados por comas) archivos para comprimir (0 si desea comprimir todos): ")
        if UnaRespuesta.find(",")>=0:
            LaLista=UnaRespuesta.split(",")
            j=0
            for xx in LaLista:
                try:
                    UnItem=int(xx.strip())
                except:
                    ElError = ElError + "El " + xx.strip() + " no es un valor válido, "
                else:
                    if UnItem>=1 and UnItem<=k+1:
                        NombreYExtension=os.path.basename(UA[UnItem-1]).split(".")
                        UnNombre=NombreYExtension[0] + ".zip"
                        ElArchivoZip=os.path.join(cls_funciones.DirectorioRelativo, "VideosComprimidos",UnNombre)
                        #Es necesario cambiar el directorio de trabajo para que el zip no incorpore el path
                        os.chdir(DirectorioBase)
                        with zipfile.ZipFile(ElArchivoZip,'w') as zip:
                            zip.write(os.path.basename(UA[UnItem-1]))
                        zip.close()
                        #el archivo fue zipeado
            print("Los archivos fueron comprimidos en: ",os.path.join(cls_funciones.DirectorioRelativo, "VideosComprimidos"))
            if ElError>"":
                print("Se encontraron los siguientes errores: ",ElError)
            sleep(5)
        else:
            #Solo eligio un archivo o todos
            try:
                UnItem = int(UnaRespuesta)
            except:
                UnItem=0
            if UnItem>=1 and UnItem<=k+1:
                NombreYExtension=os.path.basename(UA[UnItem-1]).split(".")
                UnNombre=NombreYExtension[0] + ".zip"
                ElArchivoZip=os.path.join(cls_funciones.DirectorioRelativo, "VideosComprimidos",UnNombre)
                #Es necesario cambiar el directorio de trabajo para que el zip no incorpore el path
                os.chdir(DirectorioBase)
                with zipfile.ZipFile(ElArchivoZip,'w') as zip:
                    zip.write(os.path.basename(UA[UnItem-1]))
                zip.close()
                #el archivo fue zipeado
                print("El archivo fue comprimido en: ",os.path.join(cls_funciones.DirectorioRelativo, "VideosComprimidos"))
                sleep(5)
            else:
                #van todos los archivos
                for ArchivoFin in UA:
                    NombreYExtension=os.path.basename(ArchivoFin).split(".")
                    UnNombre=NombreYExtension[0] + ".zip"
                    ElArchivoZip=os.path.join(cls_funciones.DirectorioRelativo, "VideosComprimidos",UnNombre)
                    #Es necesario cambiar el directorio de trabajo para que el zip no incorpore el path
                    os.chdir(DirectorioBase)
                    with zipfile.ZipFile(ElArchivoZip,'w') as zip:
                        zip.write(os.path.basename(ArchivoFin))
                    zip.close()
                    #el archivo fue zipeado
                print("Los archivos fueron comprimidos en: ",os.path.join(cls_funciones.DirectorioRelativo, "VideosComprimidos"))
                sleep(5)
    else:
        print("No fue posible encontrar archivos que comprimir")
        sleep(5)
def DescomprimaVideos():
    #Debe permitir al usuario elegir que videos va a comprimir, puede utilizar videosdescargados o seleccionar otra carpeta
    LosArchivos=MuestreArchivos(os.path.join(cls_funciones.DirectorioRelativo, "VideosComprimidos"))
    if len(LosArchivos)<=0:
        #No hay archivos
        print("No hemos encontrado archivos que descomprimir en el directorio por default, ")
        UnDirectorio=input("Ingrese el directorio donde se encuentran los archivos que desea descomprimir: ")
        UnDirectorio.strip(os.sep)
        EncontroDirectorio=False
        if UnDirectorio=="":
            print("El directorio {0} No Existe".format(UnDirectorio))
            sleep(5)
        elif not os.path.isdir(UnDirectorio):
            print("El directorio {0} No Existe".format(UnDirectorio))
            sleep(5)
        else:
            LosArchivos=MuestreArchivos(UnDirectorio)
            if len(LosArchivos)>0:
                EncontroDirectorio=True
    else:
        EncontroDirectorio=True

    if EncontroDirectorio:
        k=0
        print("Se encontraron los siguientes archivos: ")
        UA=[]
        for UnArchivo in LosArchivos:
            NombreYExtension=os.path.basename(UnArchivo).split(".")
            if NombreYExtension[1].upper()=="ZIP":
                UA.append(UnArchivo)
                k+=1
                print("{0}) {1}".format(k,UnArchivo))
        print("")
        ElError=""
        if len(UA)>0:
            UnaRespuesta=input("Por favor, seleccione uno (#) o varios (# separados por comas) archivos para descomprimir (0 si desea descomprimir todos): ")
            if UnaRespuesta.find(",")>=0:
                LaLista=UnaRespuesta.split(",")
                j=0
                for xx in LaLista:
                    try:
                        UnItem=int(xx.strip())
                    except:
                        ElError = ElError + "El " + xx.strip() + " no es un valor válido, "
                    else:
                        if UnItem>=1 and UnItem<=k+1:
                            UnNombre=os.path.basename(UA[UnItem-1])
                            ElArchivoZip=os.path.join(cls_funciones.DirectorioRelativo, "VideosComprimidos",UnNombre)
                            with zipfile.ZipFile(ElArchivoZip,'r') as zip:
                                zip.extractall(os.path.join(cls_funciones.DirectorioRelativo, "VideosSinCompresion"))
                            zip.close()
                            #el archivo fue deszipeado
                print("Los archivos fueron descomprimidos en: ",os.path.join(cls_funciones.DirectorioRelativo, "VideosSinCompresion"))
                if ElError>"":
                    print("Se encontraron los siguientes errores: ",ElError)
                sleep(5)
            else:
                #Solo eligio un archivo o todos
                try:
                    UnItem = int(UnaRespuesta)
                except:
                    UnItem=0
                if UnItem>=1 and UnItem<=k+1:
                    UnNombre=os.path.basename(UA[UnItem-1])
                    ElArchivoZip=os.path.join(cls_funciones.DirectorioRelativo, "VideosComprimidos",UnNombre)
                    with zipfile.ZipFile(ElArchivoZip,'r') as zip:
                        zip.extractall(os.path.join(cls_funciones.DirectorioRelativo, "VideosSinCompresion"))
                    zip.close()
                    #el archivo fue zipeado
                    print("El archivo fue descomprimido en: ",os.path.join(cls_funciones.DirectorioRelativo, "VideosSinCompresion"))
                    sleep(5)
                else:
                    #van todos los archivos
                    for ArchivoFin in UA:
                        UnNombre=os.path.basename(ArchivoFin)
                        ElArchivoZip=os.path.join(cls_funciones.DirectorioRelativo, "VideosComprimidos",UnNombre)
                        with zipfile.ZipFile(ElArchivoZip,'r') as zip:
                            zip.extractall(os.path.join(cls_funciones.DirectorioRelativo, "VideosSinCompresion"))
                        zip.close()
                        #el archivo fue zipeado
                    print("Los archivos fueron descomprimidos en: ",os.path.join(cls_funciones.DirectorioRelativo, "VideosSinCompresion"))
                    sleep(5)
        else:
            print("No se encontraron archivos que descomprimir")
            sleep(5)
    else:
        print("No fue posible encontrar archivos que descomprimir")
        sleep(5)

def ComprimaDescomprimaVideos():
    if not os.path.isdir(os.path.join(cls_funciones.DirectorioRelativo, "VideosSinCompresion")):
        print("El subdirectorio de videos sin compresión no existe, por favor verifique")
    elif not os.path.isdir(os.path.join(cls_funciones.DirectorioRelativo, "VideosComprimidos")):
        print("El subdirectorio de videos comprimidos no existe, por favor verifique")
    else: #si existen los subdirectorios para trabajar
        SeSale=False
        UnaOpcion=0
        while not SeSale:
            # Limpiar pantalla
            cls_funciones.CS()
            # Muestra el menú principal
            print("Menú Compresión/Descompresión")
            print("")
            print("1) Comprimir Videos")
            print("2) Descomprimir Videos")
            print("3) Salida")
            print("")
            OpcionValida=False
            # Se solicita el ingreso de una opción válida entre 1 y 3
            UnaOpcion,OpcionValida=cls_funciones.IngreseNumero("Ingrese una Opción:",1,3)
            if not OpcionValida: # La opción seleccionada no es válida
                print("La opción seleccionada no es válida, por favor, revise su selección")
                sleep(5)
            elif UnaOpcion==3: # Seleccionó la opcion 3: Salir del menú
                SeSale=True
            elif UnaOpcion==1: #Comprimir archivos de video
                ComprimaVideos()
            elif UnaOpcion==2: #Descomprimir videos
                DescomprimaVideos()


#Inicio del programa principal
SeSale = False
UnaOpcion=-1
while not SeSale:
    # Limpiar pantalla
    cls_funciones.CS()
    # Muestra el menú principal
    print("Menú Principal")
    print("")
    print("0) Directorio de Trabajo")
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
    UnaOpcion,OpcionValida=cls_funciones.IngreseNumero("Ingrese una Opción:",0,7)
    if not OpcionValida: # La opción seleccionada no es válida
        print("La opción seleccionada no es válida, por favor, revise su selección")
        sleep(5)
    elif UnaOpcion==7: # Seleccionó la opcion 7: Salir del programa
        SeSale=True
    elif UnaOpcion==0: #Manejar el path
        ManejoDePath()
    elif cls_funciones.DirectorioRelativo=="":
        print("No ha definido un directorio de trabajo, por favor, seleccione la opción 0 antes de continuar")
        sleep(5)
    elif UnaOpcion==1: #Selecciono la opción 1: Búsqueda de videos
        if cls_funciones.I>=0:
            # Existen datos en la lista de videos
            xy=input("Ya tiene una lista cargada, desea borrala (S/N)?")
            xy=xy.strip()
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
            DescargueLosVideos("")
        else:
            # La lista de videos esta vacía
            print("Aún no ha almacenado videos, por favor, seleccione la opción 1 primero")
            sleep(5)
    elif UnaOpcion==3: #Zip or Unzip Files
        if cls_funciones.I>=0:
            ComprimaDescomprimaVideos()
        else:
            # La lista de videos esta vacía
            print("Aún no ha almacenado videos, por favor, seleccione la opción 1 primero")
            sleep(5)
    elif UnaOpcion==4: #Seleccionar frames
        if cls_funciones.I>=0:
            BuscarFrames()
        else:
            print("Aún no ha almacenado videos, por favor, seleccione la opción 1 primero")
            sleep(5)
print("El usuario salio del programa")

