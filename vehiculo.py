class Vehiculo:
    def __init__(self, patente, marca, modelo, año, capacidad, estado):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad = capacidad
        self.estado = estado

    def mostrar_datos(self):
        print({"patente"},{"marca"},{"modelo"},{"año"},{"capacidad"},{"estado"})
        

     