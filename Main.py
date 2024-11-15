import gestion_estudiante
import gestion_cursos
import gestion_universidad
import json

def menu():
    while True:
        print("\nMenú Principal")
        print("1. Gestión de Estudiantes")
        print("2. Gestión de Cursos")
        print("3. Gestión de la Universidad")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestion_estudiante.menu_estudiantes()
        elif opcion == '2':
            gestion_cursos.menu_cursos()
        elif opcion == '3':
            gestion_universidad.menu_universidad()
        elif opcion == '4':
            # Guardar los estudiantes en un archivo JSON antes de salir
            with open("estudiantes.json", "w") as file:
                json.dump(gestion_estudiante.estudiantes_dict, file)
            print("Saliendo del sistema. Datos guardados.")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

# Ejecutar el menú principal
menu()
