class ListaCitas:
    def __init__(self):
        self.cabeza = None  # Nodo inicial de la lista

    def agregar_cita(self, cita):
       
        nuevo_nodo = NodoCita(cita)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_citas(self):
      
        actual = self.cabeza
        while actual:
            print(actual.mostrar_nodo())
            print("-" * 30)  # Separador entre citas
            actual = actual.siguiente


    def contar_citas_en_fecha(self, fecha):
    
        actual = self.cabeza
        contador = 0
        while actual:
            # Compara sólo la fecha (día, mes, año), sin la hora
            if actual.cita.fecha.date() == fecha.date():
                contador += 1
            actual = actual.siguiente
        return contador
