import webbrowser
def Opcion2():
    QueRegresa=False
    QueError = ""
    try:
        Enlace="www.github.com"
        webbrowser.open(Enlace, new=2)
        QueRegresa=True
    except:
        QueError = "Hubo un error"
        QueRegresa=False
    return QueRegresa,QueError