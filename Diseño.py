registro={}
while True:
    print("••••••Menú Principal••••••")
    print("1. Registrar pacientes")
    print("2. Buscar pacientes")
    print("3. Eleminar pacientes")
    print("4. ")
    print("5. Salir")
    opcion=int("Seleccione una opcion: ")
    match opcion:
        case "1":
            print("Registrar pacientes")
            cantidad = int(input("\nIngrese la cantidad de pacientes: "))
            for i in range(cantidad):
                print(f"\nEstudiante No.{i + 1}")
                carnet = int(input("Ingrese codigo de paciente: "))
                nombre = input("Ingrese el nombre completo del paciente: ")
                edad=int("Ingrese la fecha de nacimiento del paciente (03/05/1919): ")