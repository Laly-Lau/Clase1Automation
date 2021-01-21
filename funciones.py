
#La variable que defina dentro de la función solo es válida si la uso dentro de ella,si la llamo fuera va a dar error
def ingresar_numero(): #defino la función que voy a utilizar en varias partes de mi programa
    numero = int (input("Ingrese número: "))
    numero = numero * 30
    print (int(numero) + 20)
    return numero

#mi_numero = ingresar_numero()    
#print (mi_numero)

def hacer_algo_con_numeros(a,b):
    return a + b    

a = 50
b = 80
mi_variable = hacer_algo_con_numeros(a,b)
print(mi_variable)
mi_variable = hacer_algo_con_numeros(30,1000)
print(mi_variable)

