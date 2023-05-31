import csv
class Vehiculo():
    def __init__(self, marca, modelo, nruedas):
        self.marca = marca
        self.modelo = modelo
        self.nruedas = nruedas

    def guardar_datos_csv(self):
        try:
            with open("vehiculos.csv","a",newline="") as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print("No existe el archivo vehiculos.csv")
        except Exception as e:
            print("Error reportado: ",e) 

    def leer_datos_csv(self):
        try:
            with open("vehiculos.csv","r") as archivo:
               vehiculos = csv.reader(archivo)
               print(f"Lista de Vehiculos {type(self).__name__}")
               for item in vehiculos:
                   vehiculo_tipo = str(self.__class__)
                   if vehiculo_tipo in item[0]:
                       print(item[1])
                       print("")
        except FileNotFoundError:
            print("No existe el archivo vehiculos.csv")
        except Exception as e:
            print("Error reportado: ",e) 

    def __str__(self):
        return f"Marca : {self.marca},Modelo: {self.modelo},{self.nruedas} ruedas"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, nruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return Vehiculo.__str__(self) + f" Velocidad: {self.velocidad} , Cc: {self.cilindraje}"


class Particular(Automovil):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindraje, npuesto):
        super().__init__(marca, modelo, nruedas, velocidad, cilindraje)
        self.npuesto = npuesto

    def get_npuesto(self):
        return self.npuesto

    def set_npuesto(self, npuesto_new):
        self.npuesto = npuesto_new

    def __str__(self):
        return Automovil.__str__(self) + f" Puestos: {self.npuesto}"

class Carga(Automovil):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindraje,carga):
        super().__init__(marca, modelo, nruedas, velocidad, cilindraje)
        self.carga = carga

    def __str__(self):
        return Automovil.__str__(self) + f" Carga: {self.carga} kg"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nruedas,tipo):
        super().__init__(marca, modelo, nruedas)
        self.tipo = tipo

    def __str__(self):
        return Vehiculo.__str__(self) + f" Tipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nruedas,tipo,nradio,cuadro,motor):
        super().__init__(marca, modelo, nruedas,tipo)
        self.nradio = nradio
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
       return Bicicleta.__str__(self) + f" Numero Radios: {self.nradio}, Cuadro: {self.cuadro} , Motor: {self.motor}"
