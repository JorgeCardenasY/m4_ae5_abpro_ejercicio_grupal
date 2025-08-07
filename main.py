"""
M4_AE5_ABPRO-Ejercicio grupal

BIKECITY

Integrantes:
* Jorge Cárdenas
* Hans Schiess
* Catalina Villegas
"""
from datetime import datetime, timedelta
from bicicleta import Bicicleta
from reserva import Reserva

# Crear bicicletas
print("=== Creación de Bicicletas ===")
bici1 = Bicicleta("B001", "Oxford", "Urbana", True, 2500)
bici2 = Bicicleta("B002", "Bianchi", "Urbana", True, 2000)
bici3 = Bicicleta("B003", "Treck", "Urbana", True, 3000)

# Mostrar información inicial
print("\n=== Información Inicial de Bicicletas ===")
bici1.mostrar_info()
bici2.mostrar_info()
bici3.mostrar_info()

# Crear fechas para la reserva
inicio = datetime.now()
termino = inicio + timedelta(hours=3)

# Proceso de reserva
print("\n=== Proceso de Reserva ===")
reserva1 = Reserva("12.345.678-9", "R001", bici1, inicio, termino)

# Mostrar proceso completo
print("\n1. Intentando realizar reserva...")
if reserva1.reservar():
    print("\n2. Calculando total...")
    total = reserva1.total_renta()
    print(f"Total a pagar: ${total}")
    
    print("\n3. Realizando pago...")
    reserva1.pagar()
    
    print("\n4. Cancelando reserva...")
    reserva1.cancelar_reserva()

# Verificar estado final
print("\n=== Estado Final de la Bicicleta ===")
bici1.mostrar_info()