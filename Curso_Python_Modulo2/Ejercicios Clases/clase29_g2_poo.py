#Definiendo Objetos

class Vehiculo:
    """
    Clase vehiculo
    """
    def __init__(self, color:str, marca:str, modelo:str, cantidad_puertas:int, nombre_propietario:str | None = "Diego") -> None:
       self.color = color
       self.marca = marca
       self.modelo = modelo
       self.cantidad_puertas = cantidad_puertas
       self.nombre_propietario = nombre_propietario
       
    def detalle(self) -> str:
        """
        Me devuelve el detalle del vehiculo
        """
        print (f"El color del  auto de: {self.nombre_propietario} marca:  {self.marca} - {self.modelo} es: {self.color}")        
auto_diego = Vehiculo("rojo", "ferrari","testarossa", 2, "Diego")
auto_diego.detalle()

auto_franco = Vehiculo("verde", "ford","taunus", 4, "franco")
auto_franco.detalle()
propietario = auto_franco.nombre_propietario
print(f" el propietario es: {propietario}")
