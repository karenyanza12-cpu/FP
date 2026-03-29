# Sistema de Registro de Estudiantes

lista_estudiantes = []

def todos():  # R
    print("------Lista de Estudiantes------")
    
    if lista_estudiantes == []:
        print("No hay estudiantes registrados")
    else:
        for estudiante in lista_estudiantes:
            print("Orden:", estudiante["Orden"])
            print("Cedula:", estudiante["Cedula"])
            print("Nombre:", estudiante["Nombre"])
            print("Nivel:", estudiante["Nivel"])
            print("Paralelo:", estudiante["Paralelo"])
            print("-"*30)

def nuevo():  # C
    print("------Nuevo Estudiante------")
    
    cedula = input("Ingrese el numero de cedula: ").strip()
    
    # validar cedula unica
    for est in lista_estudiantes:
        if est["Cedula"] == cedula:
            print("La cedula ya existe")
            return
    
    estudiante = {
        "Orden": len(lista_estudiantes) + 1,
        "Cedula": cedula,
        "Nombre": input("Ingrese el nombre: ").strip(),
        "Nivel": input("Ingrese el nivel: ").strip(),
        "Paralelo": input("Ingrese el paralelo: ").strip()
    }
    
    lista_estudiantes.append(estudiante)
    
    print("Se guardo correctamente")
    print("-"*50)

def actualizar():  # U
    print("------Actualizacion de Estudiantes------")
    
    todos()
    
    cedula = input("Ingrese la cedula del estudiante: ").strip()
    
    for estudiante in lista_estudiantes:
        if estudiante["Cedula"] == cedula:
            estudiante["Nombre"] = input("Nuevo nombre: ").strip()
            estudiante["Nivel"] = input("Nuevo nivel: ").strip()
            estudiante["Paralelo"] = input("Nuevo paralelo: ").strip()
            
            print("Se actualizo correctamente")
            print("-"*50)
            return
    
    print("No se encontro el estudiante")

def eliminar():  # D
    print("------Eliminar Estudiante------")
    
    todos()
    
    cedula = input("Ingrese la cedula del estudiante: ").strip()
    
    for estudiante in lista_estudiantes:
        if estudiante["Cedula"] == cedula:
            lista_estudiantes.remove(estudiante)
            print("Se elimino correctamente")
            print("-"*50)
            return
    
    print("No se encontro el estudiante")

# Menu Principal 
while True:
    print("\nBienvenido al Sistema de Registro de Estudiantes")
    print("1. Lista de estudiantes")
    print("2. Nuevo estudiante")
    print("3. Actualizar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")
    
    opcion = input("Ingrese una opcion: ")
    
    if opcion == "1":
        todos()
    elif opcion == "2":
        nuevo()
    elif opcion == "3":
        actualizar()
    elif opcion == "4":
        eliminar()
    elif opcion == "5":
        print("Gracias por usar el sistema")
        break
    else:
        print("Opcion incorrecta")