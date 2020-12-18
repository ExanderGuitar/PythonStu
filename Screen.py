import ScreenLines as sl

class Screen():
    """Genera un objeto Screen para mostrar una interfaz"""
    
    def __init__(self, ancho=40, largo=20, estilo="@"):
        self.ancho       = ancho
        self.largo       = largo 
        self.estilo      = estilo
        self.listaLineas = []
        self.lineaHueca = sl.ScreenLines(ancho, estilo)
        self.lineaBorde = sl.ScreenLines(ancho, estilo)

    def initScreenDefecto(self):
        """Crea un Screen por defecto"""
        self.lineaHueca.initLineaMedio()
        self.lineaBorde.initLineaBorde()

        for i in range(0, self.largo):
            self.listaLineas.append(self.lineaHueca)
        
        self.listaLineas[0] = self.lineaBorde
        self.listaLineas[self.largo-1] = self.lineaBorde

    def initScreen(self):
        """Crea el Screen con las líneas"""
        for i in range(0, self.largo):
            self.listaLineas.append(self.lineaBorde)

    def insertarLinea(self, pos, linea):
        self.listaLineas[pos] = linea

    def printScreen(self):
        """Imprime el contenido del Screen"""
        for i in self.listaLineas:
            i.printLinea()
            print("")
