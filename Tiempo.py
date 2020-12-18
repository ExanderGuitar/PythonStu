from time import *

class Tiempo():

    def __init__(self):
        self.tiempo_crudo = time()
        self.tiempo_org = localtime(time())
        self.anio = self.tiempo_org[0]
        self.mes = self.tiempo_org[1]
        self.dia = self.tiempo_org[2]
        self.hora = self.tiempo_org[3]
        self.minuto = self.tiempo_org[4]
        self.segundo = self.tiempo_org[5]
        self.dia_semana = self.tiempo_org[6]
        self.dia_anio = self.tiempo_org[7]

    def imprimirFecha(self):
        print("%i/%i/%i" % (self.hora, self.mes, self.anio))
        

    def imprimirTodo(self):
        print(self.tiempo_crudo)
        print(self.tiempo_org)    
