cursos = ['modelamiento de datos', 'lenguaje programacion', 'ingles', 'taller de creatividad']
from gestion_estudiante import estudiantes_dict

def registrar_calificaciones():
    try:
        for rut, datos in estudiantes_dict.items():
            print(f"Estudiante: {datos['nombre']}")
            for i, curso in enumerate(cursos):
                print(f"Curso: {curso}, Nota: {datos['calificaciones'][i]}")
    except Exception as e:
        print(f"Error al registrar calificaciones: {e}")

def agregar_curso():
    try:
        nuevo_curso = input("Ingrese el nombre del nuevo curso: ")
        cursos.append(nuevo_curso)
        print(f"Curso '{nuevo_curso}' agregado exitosamente.")
    except Exception as e:
        print(f"Error al agregar curso: {e}")

def menu_cursos():
    while True:
        print("\nGestión de Cursos")
        print("1. Ver Calificaciones")
        print("2. Agregar Nuevo Curso")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        try:
            if opcion == '1':
                registrar_calificaciones()
            elif opcion == '2':
                agregar_curso()
            elif opcion == '3':
                break
            else:
                raise ValueError("Opción no válida. Intente de nuevo.")
        except ValueError as e:
            print(e)
