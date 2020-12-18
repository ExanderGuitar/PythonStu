import Screen as sc
import ScreenLines as sl

ANCHO = 80
LARGO = 20 
ESTILO = "#"

#crear objeto de clase 
#nombreObj = nombreArchivo.nombreClase(parametros)

pantalla = sc.Screen(ANCHO, LARGO, ESTILO)

pantalla.initScreenDefecto()

pantalla.printScreen()

line1 = sl.ScreenLines(ANCHO, ESTILO) 
line1.initLineaMedio() 
data1 = ["Nombre: ", "Alejandro"]
line1.ponerDatos(data1, "i")

line2 = sl.ScreenLines(ANCHO, ESTILO)
line2.initLineaMedio()
data2 = ["Apellido: ", "García"]
line2.ponerDatos(data2, "i")

line3 = sl.ScreenLines(ANCHO, ESTILO)
line3.initLineaMedio()
data3 = ["Apellido: ", "Surio"]
line3.ponerDatos(data3, "i")

pantalla.insertarLinea(2, line1)
pantalla.insertarLinea(3, line2)
pantalla.insertarLinea(4, line3)
pantalla.printScreen()
