pacientes={}
def registrar():
    print("Registrar pacientes.")
    codigopaciente=input("Código del paciente (o 'regresar'): ")
    if codigopaciente == "regresar":
        return
    if codigopaciente in pacientes:
        print("Ese código ya esta registrado.")
        return
    nombre=input("Nombre completo del paciente: ")
    edad=input("Edad (ej. 28 años): ")
    pacientes[codigopaciente]={
        "nombre":nombre,
        "edad":edad
    }
    print("El paciente fue registrado correctamente.")
def mostrar():
    print("Mostrar Pacientes")
    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        for codigopaciente,datos in pacientes.items():
            print(f"{datos['nombre']} - Edad: {datos['edad']} - Codigo: {codigopaciente}")
    input("\nPresione la tecla enter para regresar al menú.")
def buscar():
    print("Buscar paciente")
    nombre=input("Nombre completo del paciente (o 'regresar'): ")
    if nombre=='regresar':
        return
    encontrado=False
    for codigopaciente,datos in pacientes.items():
        if nombre in datos['nombre']:
            print(f"{datos['nombre']} - Edad: {datos['edad']} - Codigo: {codigopaciente}")
            encontrado=True
    if not encontrado:
        print("No se encontró al paciente.")
    input("\nPresione la tecla enter para regresar al menú.")
def eliminar():
    print("Eliminar Paciente")
    codigopaciente=input("Código a eliminar (o 'regresar'): ")
    if codigopaciente == "regresar":
        return
    if codigopaciente not in pacientes:
        print("Codigo no encontrado.")
        return
    print(f"Paciente encontrado {pacientes[codigopaciente]['nombre']} - Edad: {pacientes[codigopaciente]['edad']}.")
    confirmacion1= input("¿Esta seguro de querer eliminar al paciente? (Sí/No): ")
    if confirmacion1 != "Si":
        print("Operación cancelada.")
        return
    confirmacion2=input("Confirme nuevamente para eliminar al paciente (Sí/No): ")
    if confirmacion2 == "Si":
        del pacientes[codigopaciente]
        print("Se elimino correctamente al paciente.")
    else:
        print("Operación cancelada.")
while True:
    print("••••••Menú Principal••••••")
    print("1. Registrar pacientes")
    print("2. Mostrar pacientes")
    print("3. Buscar pacientes")
    print("4. Eleminar pacientes")
    print("5. Salir")
    opcion=input("Seleccione una opcion (1 a 5): ")
    match opcion:
        case "1":
            registrar()
        case "2":
            mostrar()
        case "3":
            buscar()
        case "4":
            eliminar()
        case "5":
            print("Saliendo del sistema de registro.")
            break
        case _:
            print("Opcion no valida.")