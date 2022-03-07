import webbrowser
def Opcion3():
    QueRegresa=False
    QueError = ""
    try:
        ElArchivo = "Archivo.txt"
        ElTexto = input("Ingrese un texto:")
        archivo=open(ElArchivo, "w")
        archivo.write(ElTexto)
        print("Archivo guardado correctamente")
        QueRegresa=True
    except:
        QueError = "Hubo un error"
    finally:
        try:
            archivo.close()
        except:
            QueError="Hubo un error y el archivo no fue abierto"
    return QueRegresa,QueError