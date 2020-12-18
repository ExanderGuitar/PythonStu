class ScreenLines ():
    
    def __init__(self, ancho, estilo="@"):
        self.ancho = ancho
        self.estilo = estilo
        self.contenido = []

    def initLineaBorde(self):
        """Genera una línea rellena del estilo"""
        for i in range(0, self.ancho):
            self.contenido.append(self.estilo) 

    def initLineaMedio(self):
        """Genera una línea solo con estilo en los bordes"""
        for i in range(0, self.ancho):
            self.contenido.append(" ")

        self.contenido[0] = self.estilo
        self.contenido[self.ancho-1] = self.estilo

    def __contarLetras(self, conjunto):
        """Cuenta las letras del conjunto de datos"""
        cantidad = 0

        for palabras in conjunto:
            for letras in palabras:
                cantidad += 1
        
        return cantidad

    def __insertarDatos(self, pos, conj):
        """Inserta las letras en la linea"""
        for palabras in conj:
            for letra in palabras:
                self.contenido[pos] = letra
                pos += 1

    def ponerDatos(self, conjunto, alineacion="i"):
        """Añade el texto en la linea y lo alinea"""

        if alineacion == "i":
            posicion = 2

            self.__insertarDatos(posicion, conjunto)
        
        elif alineacion == "d":
            cantidad = self.__contarLetras(conjunto)
            posicion = len(self.contenido) - cantidad - 2

            self.__insertarDatos(posicion, conjunto)

        elif alineacion == "c":
            cantidad = self.__contarLetras(conjunto)
            posicion = int((len(self.contenido) - cantidad) / 2)

            self.__insertarDatos(posicion, conjunto)
 
    def borrarLinea(self):
        """Borra el contenido de una linea"""
        self.contenido.clear()

    def printLinea(self):
        """Imprime el contenido de la línea"""
        for i in self.contenido:
            print(i, end="")
