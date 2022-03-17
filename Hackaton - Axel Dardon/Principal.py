# Se importa rutina sleep para permitir desplegar mensajes por un tiempo definido
from time import sleep
# Funciones incluye subrutinas comunes para todos los programas
import Funciones
# Opcion1 contiene las funciones relacionadas con la opcion 1 del menú
import Opcion1
# Opcion2 contiene las funciones relacionadas con la opcion 2 del menú
import Opcion2

SeSale = False
UnaOpcion=0
while not SeSale:
    # Limpiar pantalla
    Funciones.CS()
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
    UnaOpcion,OpcionValida=Funciones.IngreseNumero("Ingrese una Opción:",1,7)
    if not OpcionValida: # La opción seleccionada no es válida
        print("La opción seleccionada no es válida, por favor, revise su selección")
        sleep(5)
    elif UnaOpcion==7: # Seleccionó la opcion 7: Salir del programa
        SeSale=True
    elif UnaOpcion==1: #Selecciono la opción 1: Búsqueda de videos
        if Funciones.I>=0:
            # Existen datos en la lista de videos
            xy=input("Ya tiene una lista cargada, desea borrala (S/N)?")
            if xy=="S" or xy=="s":
                # Limpie la lista y coloque I en menos uno para indicar que no hay lista disponible
                Funciones.V.clear()
                Funciones.I=-1
                # Haga la búsqueda de videos como si fuera la primera vez
                Opcion1.BuscarVideos()
            else:
                # Muestre los videos que el usuario seleccione de la lista existente
                Opcion1.MostrarVideos()
        else:
            # Busque videos porque la lista esta vacía
            Opcion1.BuscarVideos()
    elif UnaOpcion==2: # Seleccionó la opción 2: Descarga de Video
        if Funciones.I>=0:
            # Existen datos en la lista
            # Descargue los videos que seleccione el usuario
            Opcion2.DescargarVideos()
        else:
            # La lista de videos esta vacía
            print("Aún no ha almacenado videos, por favor, seleccione la opción 1 primero")
            sleep(5)

print("El usuario salio del programa")
