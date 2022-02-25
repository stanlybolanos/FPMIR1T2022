def Sumatoria(ElNum):
    if ElNum==1:
        return 1
    else:
        return ElNum+Sumatoria(ElNum-1)
Num1=int(input("Ingrese Ultimo Numero a generar:"))
print(Sumatoria(Num1))