from pasajero import Pasajero
from conductor import Conductor
from vehiculo import Vehiculo
from pago import Pago


def main():
    pass
    # Crear pasajeros#
    pasajero2 = Pasajero(1,"Pablo Picasso","pablo.picasso@gmail.com",123456789, "Debito")
    pasajero1 = Pasajero(2,"Marcelo Perez","marcelo.perez@gmail.com",987654321, "Efectivo")

    # Crear vehículos#
    vehiculo1 = Vehiculo(123-456,"KIA","Street","2023",4,"")
    vehiculo2 = Vehiculo(123-456,"KIA","Street","2023",4,"")

    # Crear conductores#
    conductor1 = Conductor(123-456,"KIA","Street","2023",4,"")
    conductor2 = Conductor(123-456,"KIA","Street","2023",4,"")

    # Actualizar teléfono#



    # Solicitar viaje
    viaje1 = pasajero1.solicitarViaje("Plaza de Armas","Universidad")
    viaje2 = pasajero2.solicitarViaje("Quinta Normal","Parque O'higgins")
    viaje3 = pasajero1.solicitarViaje("Tobalaba","Plaza Puente Alto")

    # Conductor acepta
    
    
    

    # Definir distancia
    viaje1.distancia = 5.0
    viaje2.distancia = 7.0
    # Calcular tarifa
    viaje1.calcularTarifa()

    # Iniciar viaje
    
    
    

    # Finalizar viaje




    # Mostrar información
    print("Estado:", viaje1.estado)
    print("Tarifa:", viaje1.tarifa)

    # Generar pago
    pago1 = Pago(1,viaje1.tarifa,pasajero1.metodoPago,"PAGADO")

    print("Monto del pago:", pago1.obtenerMonto())

    pago1.generarComprobante()



    # Calificar viaje



if __name__ == "__main__":
    main()