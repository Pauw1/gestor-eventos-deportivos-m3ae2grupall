opcion = ""

print("Bienvenido al sistema de registro de eventos deportivos")

while True:

    print("1- Registrar evento deportivo")
    print("2- inscribir usuarios para cada evento")
    print("3- asignar usuarios a equipos")
    print("4- Consultar los eventos por estado.")
    print("5- Gestionar la información de los participantes")
    print("6- Administrar el proceso de inscripción y asignación de equipos")

    opcion = input("Seleccione 1-6 segun que necesite hacer: ")

    if opcion == 1:
        nombre = input("Ingrese el nombre del evento: ")
        fecha = input("Ingrese la fecha del evento en formato DD/MM/AA: ")
        tipoDeEvento = input("Ingrese el tipo de evento: ")
        estado = input("Ingrese el estado del evento: ")
    
    elif opcion == 2:
        usuario = input("ingrese el usuario: ")

    elif opcion == 3:
        print("Prueba Asignar usuarios a equipos.")


    elif opcion == 4:
        print("prueba Consultar los eventos por estado")

    elif opcion == 5:
        print("prueba Gestionar la información de los participantes.")

    elif opcion == 6:
        print("Prueba Administrar el proceso de inscripción y asignación de equipos.")

    else:
        print("Elija una opcion valida")
