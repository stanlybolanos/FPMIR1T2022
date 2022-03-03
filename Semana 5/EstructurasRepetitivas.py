

#CONTEO DE DIGITOS
Num1=int(input("ingrese numero:"))
Contador=0
NuevoNum1=Num1
while(NuevoNum1!=0):
    Contador+=1
    NuevoNum1=NuevoNum1//10
   
print("El numero",Num1,"Tiene",Contador,"digitos")

#CONTEO PARES E IMPARES
Num1=int(input("ingrese numero:"))
ContadorPares=0
ContadorImpares=0
for i in range(1,Num1+1):
    if (i%2==0):
        ContadorPares+=1
    elif(i%3==0):
        ContadorImpares+=1

print("El conteo de numeros pares es:",ContadorPares)
print("El conteo de numeros impares es:",ContadorImpares)

#FOR ANIDADOS - SECUENCIA DE NUMEROS
Num1=int(input("ingrese numero:"))
for i in range(1,Num1+1):
    for x in range(1,i+1):
        print(x, end=" ")
    print("")

#NUMEROS IMPARES EN RANGO
Num1=int(input("ingrese numero 1:"))
Num2=int(input("ingrese numero 2:"))
for i in range (Num1,Num2+1):
    for x in range(2,i):
        if(i%x==0):            
            break
    else:
        print("el numero:",i,"es numero primo")

#Fibonacci
Num1=int(input("ingrese numero 1:"))
primernum=0
segundonum=1
secuencia=0
if(Num1<2):
    print("ingrese un numero mayor a 2")
    exit()
print(primernum,end=" ")
print(segundonum,end=" ")
for i in range(3,Num1+1):
    secuencia=primernum+segundonum
    print(secuencia,end=" ")
    primernum=segundonum
    segundonum=secuencia

Num1=int(input("ingrese numero 1:"))
Suma=0
for i in range(1,Num1+1):
    Suma+=i
print("La suma de los numeros es:",Suma)


def SumaRecursiva(Num):
    if(Num==1):
        return 1
    else:
        return Num+SumaRecursiva(Num-1)

Num1=int(input("ingrese numero 1:"))
print("La suma recursiva de los numeros es:",SumaRecursiva(Num1))


def FibonacciRecursivo(numfibonacci1,
numfibonacci2,
ConteoFibonacci,
Limite):
    if(ConteoFibonacci==Limite):
        return numfibonacci2
    else:
        print(numfibonacci2,end=" ")
        return FibonacciRecursivo(numfibonacci2,
        numfibonacci1+numfibonacci2,
        ConteoFibonacci+1,Limite)
         

Num1=int(input("ingrese numero 1:"))
primernum=0
segundonum=1
secuencia=0
if(Num1<2):
    print("ingrese un numero mayor a 2")
    exit()
print(primernum,end=" ")
FibonacciRecursivo(primernum,segundonum,0,Num1-1)