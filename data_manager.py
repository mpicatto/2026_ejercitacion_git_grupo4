inventario = []

def agregar_arbol(especie, estado, ubicacion):
    nuevo_arbol = {
        "especie": especie,
        "estado": estado,
        "ubicacion": ubicacion
    }
    inventario.append(nuevo_arbol)
    return "Árbol agregado correctamente"