
#Conteo de digitos
Num1=int(input("Escriba un numero:"))
ConteoDigitos=0
Numero=Num1
while(Numero!=0):
    ConteoDigitos+=1
    Numero=Numero//10
print("El numero:",Num1,"tiene los siguientes digitos:",ConteoDigitos)

#Conteo de numeros pares e impares
Num1=int(input("Escriba un numero:"))
Listado=list(range(1,Num1+1))
ContadorPares=0
ContadorImpares=0
for i in Listado:
    if(i%2==0):
        ContadorPares+=1
    elif(i%3==0):
        ContadorImpares+=1
print("El conteo de numeros pares es:",ContadorPares)
print("El conteo de numeros impares es:",ContadorImpares)

#Ciclos anidados
Num1=int(input("Escriba un numero:"))
for i in range(1,Num1+1):
    for y in range(1,i+1):
        print(y, end=" ")
    print("")

#Numeros primos ciclos break
Num1=int(input("Escriba un numero 1:"))
Num2=int(input("Escriba un numero 2:"))
for i in range(Num1,Num2+1):
    for x in range(2,i):
        if(i%x==0):
            break
    else:
        print("Encontre el numero primo:",i)

#Secuencia Fibbonacci
Num1=int(input("Escriba un numero:"))
if(Num1<2):
    print("Porfavor ingrese un numero mayor a 2")
    exit()
PrimerNumero=0
SegundoNumero=1
print(PrimerNumero,end=" ")
print(SegundoNumero,end=" ")
for i in range(3,Num1+1):
    SiguienteSecuencia=PrimerNumero+SegundoNumero
    print(SiguienteSecuencia,end=" ")
    PrimerNumero=SegundoNumero
    SegundoNumero=SiguienteSecuencia

#Suma de numeros no recursivo
Num1=int(input("Escriba un numero:"))
Sumatoria=0
for i in range(1,Num1+1):
    Sumatoria+=i

print("La suma de los numeros 1 hasta",Num1,"es de:",Sumatoria)

#suma de numeros recursivo
Num1=int(input("Escriba un numero:"))
def SumatoriaRecursiva(Num1):
    if(Num1==1):
        return 1
    else:
        return Num1+SumatoriaRecursiva(Num1-1)


print("La suma de los numeros 1 hasta",Num1,"es de:",SumatoriaRecursiva(Num1))


#Fibonacci recursivo
Num1=int(input("Escriba un numero:"))
if(Num1<2):
    print("Porfavor ingrese un numero mayor a 2")
    exit()
PrimerNumero=0
SegundoNumero=1
print(PrimerNumero,end=" ")

def FibonacciRecursivo(PrimerNum,SegundoNum,ConteoSecuencia,Limite):
    if(ConteoSecuencia==Limite):
        return SegundoNum
    else:
        print(SegundoNum, end=" ")
        return FibonacciRecursivo(SegundoNum,PrimerNum+SegundoNum,ConteoSecuencia+1,Limite)

FibonacciRecursivo(PrimerNumero,SegundoNumero,1,Num1)