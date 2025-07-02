

opcion = ""

class Evento:
    def __init__(self,nombre,fecha,tipoDeEvento,estado):
        self.nombre = nombre
        self.fecha = fecha
        self.tipoDeEvento = tipoDeEvento
        self.estado = estado 

    def imprimir_evento(self):
        print(f"{self.nombre} {self.fecha} {self.tipoDeEvento} {self.estado}")

class  Participante:
    def __init__(self,nombre,edad,evento_asociado,equipo_asignado):
        self.nombre = nombre
        self.edad = edad
        self.evento_asociado = evento_asociado
        self.equipo_asignado = equipo_asignado

    def imprmir_participante(self):
        print(f"{self.nombre} {self.edad} {self.evento_asociado} {self.equipo_asignado}")


class Equipo:
    def __init__(self,nombre,integrantes):
        self.nombre = nombre
        self.integrantes = integrantes

    def imprimir_equipo(self):
        print(f"Equipo: {self.nombre}")
        print("Integrantes:")
        for integrante in self.integrantes:
            print(f"- {integrante}")

print("Bienvenido al sistema de registro de eventos deportivos")

while True:

    print("1- Registrar evento deportivo")
    print("2- inscribir usuarios para cada evento")
    print("3- asignar usuarios a equipos")
    print("4- Consultar los eventos por estado.")
    print("5- Gestionar la información de los participantes")
    print("6- Administrar el proceso de inscripción y asignación de equipos")

    opcion = input("Seleccione 1-6 segun que necesite hacer: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del evento: ")
        fecha = input("Ingrese la fecha del evento en formato DD/MM/AA: ")
        tipoDeEvento = input("Ingrese el tipo de evento: ")
        estado = input("Ingrese el estado del evento: ")
    
        nuevo_evento = Evento(nombre,fecha, tipoDeEvento,estado)

        print("prueba")
        nuevo_evento


    elif opcion == "2":
        usuario = input("ingrese el usuario: ")

    elif opcion == "3":
        print("Prueba Asignar usuarios a equipos.")


    elif opcion == "4":
        print("prueba Consultar los eventos por estado")

    elif opcion == "5":
        print("prueba Gestionar la información de los participantes.")

    elif opcion == "6":
        print("Prueba Administrar el proceso de inscripción y asignación de equipos.")

    else:
        print("Elija una opcion valida")
    