from clases import Vehiculo, Automovil

instancias = []

cantidad = int(input("Cuantos Vehiculos desea insertar: "))

for i in range(cantidad):
    print(f"Datos del automovil {i+1}")
    marca = input("Inserte la marca del automovil: ")
    modelo = input("Inserte el modelo: ")
    nruedas = int(input("Inserte el numero de ruedas: "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindraje = int(input("Inserte el cilindraje en cc: "))
    print("")
    auto = Automovil(marca,modelo,nruedas,velocidad,cilindraje)
    instancias.append(auto)


print("Imprimiendo por pantalla los Vehiculos: ")

for index,item in enumerate(instancias):
    print(f"Datos del automovil {index + 1} : Marca {item.marca}, Modelo {item.modelo}, {item.nruedas} ruedas, {item.velocidad} Km/h, {item.cilindraje} cc")