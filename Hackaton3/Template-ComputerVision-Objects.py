import os #libreria para trabjar con paths
import json #librearia para procesar JSON
from msrest.authentication import CognitiveServicesCredentials #Funcion para conectarse a Computer Vision usando KEY y Endpoint
from azure.cognitiveservices.vision.computervision import ComputerVisionClient #Funcion para llamar al API y procesar contenido
from tkinter import * #Libreria que permite abrir archivos
import tkinter.filedialog as fd #Libreria que permite mostrar ventana para seleccionar archivos

#Codigo para abrir JSON y guardar KEY y ENDPOINT
credenciales = json.load(open("MyPathDeArchivo.JSON"))#Este debe de ser el path donde se encuentra su archivo JSON
API_KEY = credenciales['API_KEY']
ENDPOINT = credenciales['ENDPOINT']

#Creacion de objeto "Computer Vision" para llamada de funciones de detectar contenido de imagenes
cv_client = ComputerVisionClient(ENDPOINT,CognitiveServicesCredentials(API_KEY)) #Generacion de cliente de Computer Vision en Azure

#Obtenemos imagenes
    #Aqui implementariamos el codigo
    #necesario para abrir archivos usando la funcion Tk()
    #Investigue como abrir archivos por medio de una ventana
    #Investigue tambien como limitar los archivos a extensiones de imagen (.jpg, .png, .bmp)

#Recorremos imagenes de lo que obtuvimos con Tk()
for Imagen in ListadoImagenes:
    #Seleccionamos imagen
    StreamImagen = open(Imagen, "rb")#Abrimos imagen a procesar
    #Llamamos API para obtener cotenido
    ContenidoImagen=cv_client.detect_objects_in_stream() #investigue que parametros se necesitan para llamar a detect_objects_in_stream
    #Iteramos sobre cotenido
    for Descripcion in ContenidoImagen.objects: #Recoremos objetos encontrado
        #Aqui mostramos contenido de los objetos encontrados
        #Tambien es IMPORTANTE mostrar la confianza como describe el enunciado
        #NO se olvide de almacenar el contenido en un listado y a que video y frame pertence para su REPORTE!!!
