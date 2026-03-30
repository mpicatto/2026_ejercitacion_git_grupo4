from data_manager import filtrar_enfermos

# Alumno 1 - Arquitecto de Datos

inventario = []




def inicializar_datos():
    global inventario
    inventario = [
        {
            "especie": "Jacarandá",
            "estado": "Saludable",
            "ubicacion": "Plaza San Martín"
        },
        {
            "especie": "Lapacho",
            "estado": "Enfermo",
            "ubicacion": "Av. Sarmiento"
        },
        {
            "especie": "Ceibo",
            "estado": "Saludable",
            "ubicacion": "Costanera"
        }
    ]
inventario = []

def agregar_arbol(especie, estado, ubicacion):
    nuevo_arbol = {
        "especie": especie,
        "estado": estado,
        "ubicacion": ubicacion
    }
    inventario.append(nuevo_arbol)
    return "Árbol agregado correctamente"


# Alumno 5:
def filtrar_enfermos():
    return [arbol for arbol in inventario if arbol["estado"] == "Enfermo"]


