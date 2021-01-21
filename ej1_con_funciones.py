# Sacar promedio
def promedio(mate, literatura, fisica):
    return (mate + literatura + fisica) / 3


# Imprimir datos
def datos_del_alumno(nombre, apellido, prom):
    print("El alumno ", nombre, apellido + " tiene como promedio ", prom)


# Ver aprobación de alumno
def estado_aprobacion(prom):
    if prom > 6:
        print("Aprobado")
        if prom >= 9:
            print("Alumno destacado")
    elif prom in r:
        print("A recuperatorio")
    else:
        print("Insuficiente")

    # Ingreso de datos


nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
mate = int(input("Ingrese nota de matemática:"))
literatura = int(input("Ingrese nota de literatura:"))
fisica = int(input("Ingrese nota de fisica:"))

r = range(4, 5, 6)
prom = promedio(mate, literatura, fisica)
datos_del_alumno(nombre, apellido, prom)
estado_aprobacion(prom)
