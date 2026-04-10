#  ================================
# SISTEMA DE GESTIÓN DE BIBLIOTECA
# ================================

libros = []      
contador_id = 1  



def buscar_por_id(id):
    """Retorna el libro con ese ID, o None si no existe."""
    return next((l for l in libros if l["id"] == id), None)

def estado(libro):
    """Retorna 'Disponible' o 'Prestado' según el libro."""
    return "Disponible" if libro["disponible"] else "Prestado"

def mostrar(libro):
    """Imprime un libro en formato legible."""
    print(f"  ID: {libro['id']} - '{libro['titulo']}' ({libro['autor']}, {libro['anio']}) [{estado(libro)}]")



def agregar_libro(titulo, autor, anio):
    """Agrega un libro validando que el año sea entero y mayor a 1900."""
    global contador_id
    if not isinstance(anio, int) or anio <= 1900:
        print(" El año debe ser un entero mayor a 1900.")
        return
    libros.append({"id": contador_id, "titulo": titulo, "autor": autor, "anio": anio, "disponible": True})
    contador_id += 1
    print(f" '{titulo}' agregado.")

def mostrar_libros():
    """Muestra el catálogo completo."""
    if not libros:
        print(" No hay libros registrados.")
        return
    print("\n CATÁLOGO:")
    [mostrar(l) for l in libros]

def buscar_libro(termino):
    """Busca libros por título o autor (coincidencia parcial)."""
    t = termino.lower()
    resultado = [l for l in libros if t in l["titulo"].lower() or t in l["autor"].lower()]
    if resultado:
        print(f"\n Resultados para '{termino}':")
        [mostrar(l) for l in resultado]
    else:
        print(f" Sin resultados para '{termino}'.")

def prestar_libro(id):
    """Marca un libro como prestado si está disponible."""
    libro = buscar_por_id(id)
    if not libro:
        print(f" No existe libro con ID {id}.")
    elif not libro["disponible"]:
        print(f" '{libro['titulo']}' ya está prestado.")
    else:
        libro["disponible"] = False
        print(f" '{libro['titulo']}' prestado.")

def devolver_libro(id):
    """Marca un libro como disponible."""
    libro = buscar_por_id(id)
    if not libro:
        print(f" No existe libro con ID {id}.")
    else:
        libro["disponible"] = True
        print(f" '{libro['titulo']}' devuelto.")

def eliminar_libro(id):
    """Elimina un libro solo si no está prestado."""
    libro = buscar_por_id(id)
    if not libro:
        print(f" No existe libro con ID {id}.")
    elif not libro["disponible"]:
        print(f" No se puede eliminar '{libro['titulo']}', está prestado.")
    else:
        libros.remove(libro)
        print(f" '{libro['titulo']}' eliminado.")



def libros_por_autor(autor):
    """Lista todos los libros de un autor específico."""
    resultado = [l for l in libros if autor.lower() in l["autor"].lower()]
    if resultado:
        print(f"\n Libros de '{autor}':")
        [print(f"  - '{l['titulo']}' ({l['anio']})") for l in resultado]
    else:
        print(f" No hay libros de '{autor}'.")

def estadisticas():
    """Muestra cantidad total, disponibles y prestados."""
    disponibles = sum(1 for l in libros if l["disponible"])
    print(f"\n Total: {len(libros)} | Disponibles: {disponibles} | Prestados: {len(libros) - disponibles}")

def exportar_a_txt():
    """Guarda todos los libros en 'biblioteca.txt'."""
    with open("biblioteca.txt", "w", encoding="utf-8") as f:
        f.write("CATÁLOGO DE BIBLIOTECA\n" + "=" * 40 + "\n")
        for l in libros:
            f.write(f"ID: {l['id']} | {l['titulo']} | {l['autor']} | {l['anio']} | {estado(l)}\n")
    print(" Exportado a 'biblioteca.txt'.")



def menu_principal():
    
    agregar_libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    agregar_libro("El Quijote", "Miguel de Cervantes", 1605)
    agregar_libro("1984", "George Orwell", 1949)

    opciones = {
        "1": ("Agregar libro",    lambda: agregar_libro(input("Título: "), input("Autor: "), int(x) if (x := input("Año: ")).isdigit() else x)),
        "2": ("Mostrar libros",   mostrar_libros),
        "3": ("Buscar libro",     lambda: buscar_libro(input("Buscar: "))),
        "4": ("Prestar libro",    lambda: prestar_libro(int(input("ID: ")))),
        "5": ("Devolver libro",   lambda: devolver_libro(int(input("ID: ")))),
        "6": ("Eliminar libro",   lambda: eliminar_libro(int(input("ID: ")))),
        "7": ("Libros por autor", lambda: libros_por_autor(input("Autor: "))),
        "8": ("Estadísticas",     estadisticas),
        "9": ("Exportar a .txt",  exportar_a_txt),
        "0": ("Salir",            None),
    }

    while True:
        print("\n" + "=" * 35)
        print("    GESTIÓN DE BIBLIOTECA")
        print("=" * 35)
        for k, (nombre, _) in opciones.items():
            print(f"  {k}. {nombre}")

        opcion = input("\nOpción: ")

        if opcion == "0":
            print(" ¡Hasta luego!")
            break
        elif opcion in opciones:
            opciones[opcion][1]()  
        else:
            print(" Opción no válida.")



if __name__ == "__main__":
    menu_principal()