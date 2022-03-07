import datetime
def Opcion1():
    QueRegresa=False
    QueError = ""
    try:
        x = datetime.datetime.now()
        print("Fecha y hora: {0}/{1}/{2} {3}:{4}:{5}".format(x.day,x.month,x.year,x.hour,x.minute,x.second))
        QueRegresa=True
    except:
        QueError = "Hubo un error"
        QueRegresa=False
    return QueRegresa,QueError
