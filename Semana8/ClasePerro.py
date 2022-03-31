class Perro:
    _ConteoVacunas=0
    def __init__(self,p_Nombre,p_Raza,p_FechaNacimiento):
        self.Nombre=p_Nombre
        self.Raza=p_Raza
        self.FechaNacimiento=p_FechaNacimiento
    
    def Ladrido(self):
        return "Woof!"
    
    @property
    def ConteoVacunas(self):
        return self._ConteoVacunas
    
    @ConteoVacunas.setter
    def ConteoVacunas(self,NuevoConteo):
        self._ConteoVacunas=NuevoConteo

class PerroPastor(Perro):
    def __init__(self,p_Nombre,p_Raza,p_FechaNacimiento, p_LargoCola):
        super().__init__(p_Nombre,p_Raza,p_FechaNacimiento)
        self.LargoCola=p_LargoCola

    def Rastrear(self):
        return "Woof! Rastreando!"
    
    def Ladrido(self, p_Animal):
        return "Woof! Encontre al animal: {0}!".format(p_Animal)

Max = Perro("Max","Chihuahua","01/01/2022")
print ("Mi perro se llama {0} es un {1} y nacio el {2} y cuando ladra hace {3}".format(Max.Nombre,Max.Raza,Max.FechaNacimiento,Max.Ladrido()))
Lassie = PerroPastor("Lassie","Colie","01/01/1990","30cm")
print ("Mi perro se llama {0} es un {1} y nacio el {2} y cuando ladra hace {3}".format(Lassie.Nombre,Lassie.Raza,Lassie.FechaNacimiento,Lassie.Ladrido("Oveja")))