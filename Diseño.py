registro={}
while True:
    print("••••••Menú Principal••••••")
    print("1. Registrar pacientes")
    print("2. Mostrar pacientes")
    print("3. Buscar pacientes")
    print("4. Eleminar pacientes")
    print("5. Salir")
    opcion=int("Seleccione una opcion: ")
    match opcion:
        case "1":
            print("Registrar pacientes")
            cantidad = int(input("\nIngrese la cantidad de pacientes: "))
            for i in range(cantidad):
                print(f"\nEstudiante No.{i + 1}")
                codigo = int(input("Ingrese codigo de paciente: "))
                nombre = input("Ingrese el nombre completo del paciente: ")
                edad=input("Ingrese la edad del paciente (18 años): ")
                registro[codigo]={
                    "nombre":nombre,
                    "edad":edad
                }
        case "2":
            print("Mostrar pacientes")
            if not registro:
                print("No se ha podido registrar pacientes")
            else:
                for codigo
