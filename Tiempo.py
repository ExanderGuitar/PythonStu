from time import *
import pathlib as pl

class Tiempo():

    def __init__(self):
        self.tiempo_crudo = time()
        self.tiempo_org = localtime(time())
        self.anio = self.tiempo_org[0]
        self.mes = self.tiempo_org[1]
        self.dia = self.tiempo_org[2]
        self.fecha = [self.dia, self.mes, self.anio]
        self.hora = self.tiempo_org[3]
        self.minuto = self.tiempo_org[4]
        self.segundo = self.tiempo_org[5]
        self.tiempo = [self.hora, self.minuto, self.segundo]
        self.dia_semana = self.tiempo_org[6]
        self.dia_anio = self.tiempo_org[7]
        self.directory = pl.Path.cwd()

    def guardar_tiempo(self):
        self.arch = self.abrir_archivo("w")

        for i in self.fecha:
            self.arch.write("%s\n" % str(i))
        for j in self.tiempo:
            self.arch.write("%s\n" % str(j))

        self.arch.close()

    def cargar_tiempo(self):
        self.arch = self.abrir_archivo("r")

        for i in range(0,3):
            self.fecha[i] = int(self.arch.readline())        
        for j in range(0,3):
            self.tiempo[j] = int(self.arch.readline())

        self.arch.close()

    def abrir_archivo(self, modo):
        try:
            open("SaveFile.txt")
        except:
            print("SaveFile.txt doesn't exists")
            self.entrada = input("Do you want to create it?(y/n): ")

            if (self.entrada == "y" or self.entrada == "Y"):
                pl.Path.cwd().joinpath("SaveFile.txt").touch()
                print("File has been created at: ", pl.Path.cwd())
                print("And now is open!")
                self.archivo = open("SaveFile.txt", modo)
                return self.archivo
            elif (self.entrada == "n" or self.entrada == "N"):
                print("I need a file to store the data!") 
            else:
                print("I can't understand you, sorry")
        else:
            print("SaveFile is in your current directory")
            print("SaveFile.txt opened!")
            self.archivo = open("SaveFile.txt", modo)
            return self.archivo

    def imprimirHora(self):
        print("%i:%i:%i" % (self.tiempo[0], self.tiempo[1], self.tiempo[2]))
    def imprimirFecha(self):
        print("%i/%i/%i" % (self.fecha[0], self.fecha[1], self.fecha[2]))
        

    def imprimirTodo(self):
        print(self.tiempo_crudo)
        print(self.tiempo_org)    

