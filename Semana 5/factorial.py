def Factorial(num):
    if (num<0):
        print("No existe el factorial para numero negativo")
        return -1
    elif ((num==0) or (num==1)):
        return 1 #El factorial de 0 y 1 es 1
    resultado=1
    i=2
    while i<=num:
        resultado+=i
        i+=1
    print("El resultado de factorial del numero:",num,"es de:",resultado)
    return resultado

numero=int(input("ingrese numero:"))
Factorial(numero)

x=(1,2,3,4,5)

for i in (1,2):
    print("yo voy a aparecer dos veces")
    for i in (1,2):
        print("yo voy a aparecer cuatro veces")


for i in range(1,6):
    print("hola2",i)
