from datetime import datetime


lista_citas = ListaCitas()


cita1 = Cita("Ana", "Luis", datetime(2024, 11, 10, 20, 0), "Café Central", "Primera cita en un ambiente relajado")
cita2 = Cita("Carlos", "María", datetime(2024, 11, 10, 18, 0), "Parque Norte", "Caminar y conversar")
cita3 = Cita("Laura", "Miguel", datetime(2024, 11, 11, 19, 0), "Restaurante Luna", "Cena romántica")


lista_citas.agregar_cita(cita1)
lista_citas.agregar_cita(cita2)
lista_citas.agregar_cita(cita3)

print("Mostrando todas las citas:")
lista_citas.mostrar_citas()

fecha_busqueda = datetime(2024, 11, 10)
num_citas = lista_citas.contar_citas_en_fecha(fecha_busqueda)
print(f"\nNúmero de citas en {fecha_busqueda.strftime('%d/%m/%Y')}: {num_citas}")
