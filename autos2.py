marcas = ["chevrolet","ford","fiat"]
cant_puertas = [2,4,5]
colores = ["blanco","azul","negro"]
ventas = []
nuevocli = "si"
i = 0
n = 1

def valida_marca (marca):
     if marca not in marcas:
        print("La marca ingresada no es correcta, puede ser Ford, chevrolet o fiat")
        marca = input ("Ingrese la marca del vehículo:")
        valida_marca(marca)

def valida_puertas (puertas):
     if puertas not in cant_puertas:
        print("La cantidad de puertas ingresada no es correcta, pueden ser 2, 4 ó 5 puertas")
        puertas = input ("Ingrese la cantidad de puertas:")
        valida_puertas(puertas)

def valida_color (color):
     if color not in colores:
        print("El color ingresado no es correcta, el color puede ser rojo, azul o negro")
        color = input ("Ingrese el color del vehículo:")
        valida_color(color)                   

def total_marca(marca):
    if marca == "ford":
        totalm =  100000
    elif marca == "chevrolet":
        totalm =  120000
    else:
        totalm =  80000        
    return totalm

def total_puertas(puertas):
    if puertas == 2:
        totalp = 50000
    elif puertas == 4:
        totalp = 65000
    else:
        totalp = 78000
    return totalp              

def total_color(color):
    if color == "blanco":
        totalc = 10000
    elif color == "azul":    
        totalc = 20000
    else:
        totalc=30000
    return totalc            


while nuevocli == "si":
    i += 1
    nombre = input ("Ingrese su nombre y apellido del comprador " + str(i) + ":")
    marca = input ("Ingrese la marca del vehículo:")
    valida_marca(marca)
    puertas = int(input ("Ingrese cantidad de puertas:"))
    valida_puertas(puertas)
    color = input ("Ingrese el color del vehículo:")
    valida_color(color)
    totalm = total_marca(marca)
    totalp = total_puertas(puertas)
    totalc = total_color(color)
    total = (totalm + totalp + totalc)
    ventas.append ({"Cliente ": i, "Nombre " :nombre, "Precio" :total})
    nuevocli = str(input ("Hay un cliente nuevo: "))
    total_clientes = i
   
if total_clientes > 50:
    for n in range(0,total_clientes):
        ventas[n]["Precio"] = (ventas[n]["Precio"] -(ventas[n]["Precio"]*0.18))
elif total_clientes in range (11,50):
    for n in range(0,total_clientes):
        ventas[n]["Precio"] = (ventas[n]["Precio"] -(ventas[n]["Precio"]*0.15))
elif total_clientes in range(6,10):
    for n in range(0,total_clientes): 
        ventas[n]["Precio"] = (ventas[n]["Precio"] -(ventas[n]["Precio"]*0.10))      
else:
    print("La venta no tiene descuentos")

print (ventas)
