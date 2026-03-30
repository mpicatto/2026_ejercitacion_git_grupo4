from data_manager import *
from data_manager import filtrar_enfermos

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ver árboles")
    print("2. Agregar árbol")
    print("3. Salir")


def main():
    inicializar_datos()

while True:
    print("\n--- Eco Tracker ---")
    print("1. Ver árboles")
    print("2. Agregar árbol")
    print("3. Ver árboles enfermos")
    print("4. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "3":
        enfermos = filtrar_enfermos()
        
        if len(enfermos) == 0:
            print("No hay árboles enfermos.")
        else:
            print("\nÁrboles enfermos:")
            for arbol in enfermos:
                print(f"- {arbol['especie']} | {arbol['ubicacion']}")


if __name__ == "__main__":
    main()