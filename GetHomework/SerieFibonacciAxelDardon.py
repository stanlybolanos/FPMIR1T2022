Num1=int(input("Ingrese Numero Num1:"))
anterior=0
actual=1
i=actual
if Num1>0:
    if Num1==1:
        print(anterior,", ",actual)
    else:
        print(anterior,", ",actual,end=", ")
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
    