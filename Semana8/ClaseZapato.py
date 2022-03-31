class Zapato:
    __TecnologiaZapato="Wide Fit Foam Running Ultra"
    __Material="Material de fibra y hule patentado"

    NombreZapateria="Payless Shoes"
    PuntoDeVenta="Centro Comercial Miraflores"

    def __init__(self,p_Talla,p_EstaEnVenta,p_Precio):
        self.Talla=p_Talla
        self.EstaEnVenta=p_EstaEnVenta
        self._Precio=p_Precio

    @property
    def Precio(self):
        return self._Precio

    @Precio.setter
    def Precio(self,NuevoPrecio):
        self._Precio=NuevoPrecio*1.12

    def MaterialZapato(self):
        return self.__Material

    @classmethod
    def CambioPuntoDeVenta(cls,NuevoPuntoDeVenta):
        Zapato.PuntoDeVenta=NuevoPuntoDeVenta

    @staticmethod
    def PrintNombreZapateria():
        return Zapato.NombreZapateria
    
print("El nombre de la zapateria es {0}".format(Zapato.PrintNombreZapateria()))

Tenis = Zapato(38,True,350.00)
print(Tenis._Zapato__TecnologiaZapato)
print("El Zapato Tenis esta en venta: {0} tiene una talla de {1} y se vende a un precio de {2}".format(Tenis.EstaEnVenta,Tenis.Talla,Tenis.Precio))
Tenis.Precio=400.00
print("El Zapato Tenis esta en venta: {0} tiene una talla de {1} y se vende a un precio de {2}".format(Tenis.EstaEnVenta,Tenis.Talla,Tenis.Precio))
print("El material del zapato Tenis es: {0}".format(Tenis.MaterialZapato()))
Bota = Zapato(40,True,500.00)
print("El zapato tenis se vende en: {0} y la bota se vende en {1}".format(Tenis.PuntoDeVenta,Bota.PuntoDeVenta))
Zapato.CambioPuntoDeVenta("Okaland Mall")
print("El zapato tenis se vende en: {0} y la bota se vende en {1}".format(Tenis.PuntoDeVenta,Bota.PuntoDeVenta))