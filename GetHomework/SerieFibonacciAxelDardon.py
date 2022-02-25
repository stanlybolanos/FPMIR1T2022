def Fibonacci1(ElNum):
    anterior=0
    actual=1
    i=actual
    if Num1>0:
        if Num1==1:
            print(str(anterior) + ", "+str(actual))
        else:
            print(str(anterior)+ ", "+str(actual),end=", ")
        while i<Num1:
            siguiente=anterior+actual
            i=siguiente
            anterior=actual
            actual=siguiente
            if i>=Num1:
                print(i)
            else:
                print(i, end=", ")
    else:
        print("No es posible realizar la secuencia")

Num1=int(input("Ingrese Ultimo Numero a generar:"))
Fibonacci1(Num1)    