#IF


Num2=int(input("ingrese numero 2:"))
"""
Num1=int(input("ingrese numero 1:"))

"""
"""
if Num1==Num2:
    print("Los numeros",Num1,"y",Num2,"si son iguales")
    #esto todavia es una linea del
#esta linea ya NO pertenece al if

if Num1>Num2:
    print("El numero",Num1,"es mayor que",Num2)

if Num2>Num1:
    print("El numero",Num2,"es mayor que",Num1)
"""

#ELIF
"""
if Num1==Num2:
    print("Los numeros",Num1,"y",Num2,"si son iguales")
elif Num1>Num2:
    print("El numero",Num1,"es mayor que",Num2)
elif Num2>Num1:
    print("El numero",Num2,"es mayor que",Num1)
else:
    print("nada de lo anterior")
"""
#ELSE
"""
ingresos=int(input("Cuales son sus ingresos:"))

if(ingresos<10000):
    print("sus ingresos son menores a 10mil")
elif (ingresos>=10000 and ingresos<=30000):
    print("sus ingersos se encuentran entre 10mil y 30mil")
else:
    print("sus ingresos no estan en ninguno de esos rangos")
"""

#IF-ELSE de una linea
"""
#if(Num1==Num2): print("los numeros",Num1,"y",Num2,"son iguales")
#print("los numeros",Num1,"y",Num2,"son iguales") if(Num1==Num2) else print("Los numeros",Num1,"y",Num2,"son diferentes")
SonIguales=(True if(Num1==Num2) else False)
print(SonIguales)
"""

#IF anidados
Num1=int(input("ingrese numero 1:"))
if(Num1%2==0):
    Num2=int(input("ingrese numero 2:"))
    if(Num2%2==0):
        print("El resultado de",Num1,"elevado a la potencia",Num2,"es:",Num1**Num2)
    else:
        print("El resutlado de",Num1,"dividido",Num2,"es:",Num1/Num2)

#pass
"""
Num1=int(input("ingrese numero 1:"))
if(Num1%2==0):
    pass
else:
    print("no fue un numero par")

#Switcher
Num1=input("ingrese numero de dia de la semana:")
DiasSemana={
    "1":"Lunes",
    "2":"Martes",
    "3":"Miercoles",
    "4":"Jueves",
    "5":"Viernes",
    "6":"Sabado",
    "7":"Domingo"
}

print("El dia de la semana para el numero",Num1,"es:",DiasSemana.get(Num1,"No es un dia de la semana"))
"""

#Excepciones
try:
    print("Estoy en el bloque de try")
    print(int(input("Numero1:"))/int(input("Numero2:")))
except ZeroDivisionError:
    print("Capture un error de division por cero")
except:
    print("Ocurrio otro error")
else:
    print("No hubieron errores")

archivo=open("c:\\temp\\prueba.txt","w")
try:
    archivo.write("Este es el nuevo contenido del archivo")
except:
    print("No se pudo escribir en el archivo")
else:
    print("archivo modificado exitosamente")
finally:
    archivo.close()
    print("se cerro el archivo exitosamente")
