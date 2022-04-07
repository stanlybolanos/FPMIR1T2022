import webbrowser
from pytube import Search

from pytube import YouTube, Playlist
import os
import requests




class Video:
    Directorio="c:\\temp\\"

    def _init_(self,p_URL,p_TituloVideo,p_TextodeBusqueda):
        self._URL=p_URL
        self._TituloVideo=p_TituloVideo
        self._TextodeBusqueda=p_TextodeBusqueda
    


    @staticmethod
    def DescargarVideo(TextoBusqueda,pathgrabado):
        busqueda=Search(TextoBusqueda)
        ResultadoSeleccionado=str(busqueda.results[0])
        IDSeleccionado=ResultadoSeleccionado[41:52]
        URLvideo="https://www.youtube.com/watch?v="+IDSeleccionado
        VideoDescargado=YouTube(URLvideo)
        VideoDescargado.streams.first().download(str(pathgrabado))
        print("El video fue descargado con exito")

## Texto busqueda
    @property
    def TextoBusqueda(self):
        return self._TextodeBusqueda

    @TextoBusqueda.setter
    def TextoBusqueda(self,NuevoTexto):
        self._TextodeBusqueda=NuevoTexto

## URL
    @property
    def URL(self):
        return self._URL

    @URL.setter
    def URL(self,NuevoURL):
        self._URL=NuevoURL

## Titulo Video
    @property
    def TituloVideo(self):
        return self._TituloVideo

    @TituloVideo.setter
    def TituloVideo(self,NuevoTituloVideo):
        self._TituloVideo=NuevoTituloVideo

class Busqueda:
    def _init_(self,p_video):
        self.Video=p_video

        
TextoBusqueda=input("Ingrese texto de busqueda:")
busqueda=Search(TextoBusqueda)
Resultadoi=str(busqueda.results[0])
IDi=Resultadoi[41:52]
LinkVideo="https://www.youtube.com/watch?v="+IDi
yt = YouTube(LinkVideo)


VideoPython=Video(LinkVideo,yt.title,TextoBusqueda)
print("El enlace del video es:", VideoPython.URL) 
print("El titulo del video es:",VideoPython.TituloVideo)
print("El directorio donde se descargara el video es",VideoPython.Directorio)
Video.DescargarVideo(VideoPython.TextoBusqueda,VideoPython.Directorio)

##Nueva busqueda con cambio de atributo
VideoPython.TextoBusqueda=input("Ingrese un nuevo texto de busquedad:")
busqueda2=Search(VideoPython.TextoBusqueda)
Resultado2=str(busqueda2.results[0])
IDi=Resultado2[41:52]
VideoPython.URL="https://www.youtube.com/watch?v="+IDi
yt2 = YouTube(VideoPython.URL)
VideoPython.TituloVideo=yt2.title
print("El enlace del video es:", VideoPython.URL) 
print("El titulo del video es:",VideoPython.TituloVideo)
print("El directorio donde se descargara el video es",VideoPython.Directorio)

Video.DescargarVideo(VideoPython.TextoBusqueda,VideoPython.Directorio)