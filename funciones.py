def ingresar_alimentos(alimentos, precios, cantidades, numero_item, nuevos_alimentos):
    for i in range(numero_item, numero_item + nuevos_alimentos):
        alimentos[i] = input(f"Ingrese el nombre del alimento {i + 1}: ")
        precios[i] = float(input(f"Ingrese el precio del alimento {i + 1}: "))
        cantidades[i] = int(input(f"Ingrese la cantidad del alimento {i + 1}: "))

def imprimir_alimentos(alimentos, precios, cantidades, n):
    print("Nombre\t\t\tPrecio\t\tCantidad")
    for i in range(n):
        print(f"{alimentos[i]:<20}\t{precios[i]:.2f}\t\t{cantidades[i]}")

def imprimir_advertencia():
    print("\nTiempo aproximado de descomposición de la carne (en días):")
    print("Carne cruda refrigerada: Pollo/pavo (1-2 días), Res/cerdo (3-5 días)")
    print("Carne cocida refrigerada: Pollo/pavo (3-4 días), Res/cerdo (3-4 días)")
    print("Carne congelada: Hasta varios meses")
    print("Condiciones ambiente: Comienza a descomponerse rápidamente")

def buscar_alimento(alimentos, nombre_alimento, n):
    for i in range(n):
        if alimentos[i] == nombre_alimento:
            return i
    return -1

def imprimir_alimento_index(alimentos, precios, cantidades, index):
    if index != -1:
        print("Los datos del alimento son:")
        print(f"Nombre: {alimentos[index]}")
        print(f"Precio: {precios[index]:.2f}")
        print(f"Cantidad: {cantidades[index]}")
        imprimir_advertencia()
    else:
        print("No existe el alimento en el inventario.")

def editar_alimento(alimentos, precios, cantidades, n):
    nombre_alimento = input("Ingrese el nombre del alimento que desea editar: ")
    index = buscar_alimento(alimentos, nombre_alimento, n)
    if index != -1:
        alimentos[index] = input("Ingrese el nuevo nombre del alimento: ")
        precios[index] = float(input("Ingrese el nuevo precio del alimento: "))
        cantidades[index] = int(input("Ingrese la nueva cantidad del alimento: "))
        print("Alimento actualizado.")
    else:
        print(f"No existe el alimento {nombre_alimento} en el inventario.")

def eliminar_alimento(alimentos, precios, cantidades, numero_item):
    nombre_alimento = input("Ingrese el nombre del alimento que desea eliminar: ")
    index = buscar_alimento(alimentos, nombre_alimento, numero_item)
    if index != -1:
        for i in range(index, numero_item - 1):
            alimentos[i] = alimentos[i + 1]
            precios[i] = precios[i + 1]
            cantidades[i] = cantidades[i + 1]
        numero_item -= 1
        print("Alimento eliminado.")
    else:
        print(f"No existe el alimento {nombre_alimento} en el inventario.")
    return numero_item

def opcion_ingresar_alimentos(alimentos, precios, cantidades, numero_item, maximo_inventario):
    nuevos_alimentos = int(input("¿Cuántos alimentos desea ingresar? "))
    if numero_item + nuevos_alimentos > maximo_inventario:
        print(f"El número máximo es {maximo_inventario - numero_item}")
        nuevos_alimentos = maximo_inventario - numero_item
    ingresar_alimentos(alimentos, precios, cantidades, numero_item, nuevos_alimentos)
    numero_item += nuevos_alimentos
    return numero_item

def opcion_buscar_alimento(alimentos, precios, cantidades, numero_item):
    nombre = input("Ingrese el nombre del alimento que desea ver: ")
    index = buscar_alimento(alimentos, nombre, numero_item)
    imprimir_alimento_index(alimentos, precios, cantidades, index)

def leer_alimentos(alimentos, alimento_doc):
    try:
        with open(alimento_doc, "r") as file:
            i = 0
            for line in file:
                if i < 10:
                    alimentos[i] = line.strip()
                    i += 1
        return i
    except FileNotFoundError:
        with open(alimento_doc, "w") as file:
            pass
        return 0

def leer_precios(precios, precios_doc, n):
    try:
        with open(precios_doc, "r") as file:
            for i in range(n):
                try:
                    precios[i] = float(file.readline().strip())
                except ValueError:
                    precios[i] = 0
    except FileNotFoundError:
        with open(precios_doc, "w") as file:
            pass

def leer_cantidades(cantidades, cantidades_doc, n):
    try:
        with open(cantidades_doc, "r") as file:
            for i in range(n):
                try:
                    cantidades[i] = int(file.readline().strip())
                except ValueError:
                    cantidades[i] = 0
    except FileNotFoundError:
        with open(cantidades_doc, "w") as file:
            pass

def guardar_alimentos(alimentos, alimento_doc, n):
    with open(alimento_doc, "w") as file:
        for i in range(n):
            file.write(f"{alimentos[i]}\n")

def guardar_precios(precios, precios_doc, n):
    with open(precios_doc, "w") as file:
        for i in range(n):
            file.write(f"{precios[i]:.2f}\n")

def guardar_cantidades(cantidades, cantidades_doc, n):
    with open(cantidades_doc, "w") as file:
        for i in range(n):
            file.write(f"{cantidades[i]}\n")