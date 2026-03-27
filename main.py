from data_manager import *


def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ver árboles")
    print("2. Agregar árbol")
    print("3. Salir")


def main():
    inicializar_datos()


    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")


        if opcion == "1":
            print("Función aún no implementada.")
       
        elif opcion == "2":
            print("Función aún no implementada.")
       
        elif opcion == "3":
            print("Saliendo del programa...")
            break
       
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()