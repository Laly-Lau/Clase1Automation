nombre = input ("Ingrese su nombre:")
apellido = input ("Ingrese su apellido:")
mate = int(input ("Ingrese nota de matemática:")) 
literatura = int(input ("Ingrese nota de literatura:")) 
fisica = int(input ("Ingrese nota de fisica:")) 


promedio = (mate + literatura + fisica)/3
r = range (4,5,6)

print ("El alumno " + nombre + " " + apellido + " " +"tiene como promedio " + str(promedio))


if promedio > 6:
    print ("Aprobado")
    if promedio >= 9:
        print ("Alumno destacado")
elif promedio in r:
    print ("A recuperatorio")  
else:
    print ("Insuficiente")    


