import Tiempo as tp

print("Tiempo nuevo")
nuevo = tp.Tiempo()
nuevo.imprimirFecha()
nuevo.imprimirHora()
nuevo.imprimirTodo()

respuesta = input("Quieres cargar otro tiempo: (y/n):")
if respuesta == "y":
    print("Cargando tiempo")
    nuevo.cargar_tiempo()
    nuevo.imprimirFecha()
    nuevo.imprimirHora()

entrada = input("Quieres guardar el tiempoa actual? (y/n):")
if entrada == "y":
    print("Guardando tiempo")
    nuevo.guardar_tiempo()

#print("Hoy es %i del %i del %i (%i/%i/%i) y son las %i:%i:%i. Es el %i dia de la semana y el %i dia del año." % (local[2], local[1], local[0], local[2], local[1], local[0], local[3], local[4], local[5], local[6] + 1, local[7]))
