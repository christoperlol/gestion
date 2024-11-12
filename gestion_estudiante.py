import json

# Diccionario de estudiantes
estudiantes_dict = {}

# Lista de cursos
cursos = ['modelamiento de datos', 'lenguaje programacion', 'ingles', 'taller de creatividad']

def registrar_estudiante():
    try:
        rut = input("Ingrese el RUT del estudiante: ")
        matricula = input("Ingrese la matrícula del estudiante: ")
        nombre = input("Ingrese el nombre completo del estudiante: ")
        calificaciones = []

        for curso in cursos:
            while True:
                try:
                    calificacion = float(input(f"Ingrese la calificación en {curso} (1-7): "))
                    if 1 <= calificacion <= 7:
                        calificaciones.append(calificacion)
                        break
                    else:
                        print("La calificación debe estar entre 1 y 7.")
                except ValueError:
                    print("Error: Ingrese un número válido.")
        
        promedio = sum(calificaciones) / len(calificaciones)
        estudiantes_dict[rut] = {
            'matricula': matricula,
            'nombre': nombre,
            'calificaciones': calificaciones,
            'promedio': promedio
        }
        print("Estudiante registrado exitosamente.\n")
    except Exception as e:
        print(f"Error al registrar estudiante: {e}")

def actualizar_estudiante():
    try:
        rut = input("Ingrese el RUT del estudiante a actualizar: ")
        if rut in estudiantes_dict:
            nombre = input("Ingrese el nuevo nombre del estudiante: ")
            calificaciones = []

            for curso in cursos:
                while True:
                    try:
                        calificacion = float(input(f"Ingrese la nueva calificación en {curso} (1-7): "))
                        if 1 <= calificacion <= 7:
                            calificaciones.append(calificacion)
                            break
                        else:
                            print("La calificación debe estar entre 1 y 7.")
                    except ValueError:
                        print("Error: Ingrese un número válido.")
            
            promedio = sum(calificaciones) / len(calificaciones)
            estudiantes_dict[rut] = {
                'nombre': nombre,
                'calificaciones': calificaciones,
                'promedio': promedio
            }
            print("Estudiante actualizado exitosamente.\n")
        else:
            print("Error: Estudiante no encontrado.\n")
    except Exception as e:
        print(f"Error al actualizar estudiante: {e}")

def eliminar_estudiante():
    try:
        rut = input("Ingrese el RUT del estudiante a eliminar: ")
        if rut in estudiantes_dict:
            with open("estudiantes_eliminados.json", "a") as file:
                json.dump(estudiantes_dict[rut], file)
                file.write("\n")
            del estudiantes_dict[rut]
            print("Estudiante eliminado y registro guardado.\n")
        else:
            print("Error: Estudiante no encontrado.\n")
    except Exception as e:
        print(f"Error al eliminar estudiante: {e}")

def visualizar_estudiantes():
    try:
        if estudiantes_dict:
            print("\nLista de Estudiantes:")
            for rut, datos in estudiantes_dict.items():
                print(f"RUT: {rut}")
                print(f"Nombre: {datos['nombre']}")
                print(f"Calificaciones: {datos['calificaciones']}")
                print(f"Promedio: {datos['promedio']:.2f}")
                print("-" * 20)
        else:
            print("No hay estudiantes registrados.\n")
    except Exception as e:
        print(f"Error al visualizar estudiantes: {e}")

def menu_estudiantes():
    while True:
        print("\nGestión de Estudiantes")
        print("1. Registrar Estudiante")
        print("2. Actualizar Estudiante")
        print("3. Eliminar Estudiante")
        print("4. Visualizar Estudiantes")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        try:
            if opcion == '1':
                registrar_estudiante()
            elif opcion == '2':
                actualizar_estudiante()
            elif opcion == '3':
                eliminar_estudiante()
            elif opcion == '4':
                visualizar_estudiantes()
            elif opcion == '5':
                break
            else:
                raise ValueError("Opción no válida. Intente de nuevo.")
        except ValueError as e:
            print(e)
