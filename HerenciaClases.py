class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False    #El objeto por defecto no va a estar en marcha
        self.acelera=False     #Porque va a estar detenido
        self.frena=False       #False porque va a estar detenido
       
    def arrancar(self):
        self.enmarcha=True
        
    def acelerar(self):
        self.acelera=True
        
    def frenar(self):
        self.frena=True
        
    def estado(self):
        print("Marca; ",self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
             self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)
        
    
#clase secundaria que va a heredar los métodos de la clase vehiculos
class Moto(Vehiculos):
    pass
miMoto=Moto("Honda","CBR")
miMoto.estado()
