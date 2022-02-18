#Num1=int(input("ingrese numero 1: "))
#Num2=int(input("ingrese numero 2: "))
#if
"""
if Num1==Num2:
    print("Los numeros", Num1, "y ", Num2, "si son iguales")

if Num1>Num2:
    print("El numero", Num1, "es mayor que ", Num2)

if Num2>Num1:
    print("El numero", Num2, "es menor que ", Num1)
"""

#elif
"""
if Num1==Num2:
    print("Los numeros", Num1, "y ", Num2, "si son iguales")

elif Num1>Num2:
    print("El numero", Num1, "es mayor que ", Num2)

elif Num2>Num1:
    print("El numero", Num2, "es menor que ", Num1)
"""
 #else
"""
 ingresos=int(input("Ingrese el monto de sus ingresos: "))
if ingresos < 10000:
    print("Sus ingresos son menores o iguales a 10,000")  
elif (ingresos>10000 and ingresos<30000):
    print("Sus ingresos están entre 10,000 y 30,000") 
else:
    print("Sus ingresos estan fuera de los rangos")
"""
#if anidados
"""
Num1=int(input("ingrese numero 1: "))
if(Num1%2==0):
    Num2=int(input("Ingrese numero2: "))
    if(Num2%2==0):
        print("E; resultado de",Num1,"elevado a la potencia", Num2,"es: ",Num1**Num2)
    else:
        print("El resultado de",Num1,"dividido",Num2,"es:",Num1/Num2)
        """
#pass
"""
Num1=int(input("ingrese numero 1: "))
if(Num1%2==0):
    pass
else:
    print("No es un numero par")
"""
#switcher
"""
Num1=int(input("ingrese numero del día de la semana: "))
DiasSemana={
    1:"Lunes",
    2:"Martes",
    3:"Miercoles",
    4:"Jueves",
    5:"Viernes",
    6:"Sábado",
    7:"Domingo",
}
print("El día de la seman para el numero",Num1,"es: ",DiasSemana.get(Num1,"No es un día de la semana"))
"""
#Excepciones
"""
try:
    print("Estoy en el bloque de try")
    (int(input("Numero1: "))/int(input("Numero2: ")))
except ZeroDivisionError:
    print("Capture un erro de división por cero")
except ValueError:
    print("Eror en el tipo de dato ingresado")
else:
    print("Es otro error")
"""


try:
    archivo=open("c:\\temp\\prueba.txt", "w")
    archivo.write("Este ese el nuevo contenido del archivo")
except:
    print("no se pudo escribir el archivo")
else: 
    print("Archivo modificado exitosamente")
finally:
    archivo.close()