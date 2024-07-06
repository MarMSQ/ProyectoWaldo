
from funciones import *
MAXIMO_INVENTARIO = 10

def main():
    alimentos = [""] * MAXIMO_INVENTARIO
    precios = [0.0] * MAXIMO_INVENTARIO
    cantidades = [0] * MAXIMO_INVENTARIO
    numero_item = 0

    numero_item = leer_alimentos(alimentos, "alimentos.txt")
    leer_precios(precios, "precios.txt", numero_item)
    leer_cantidades(cantidades, "cantidades.txt", numero_item)

    print("BIENVENIDOS A CARNICERIA WALDO")

    while True:
        print("Seleccione una opción:")
        print("1. Ingresar Alimentos")
        print("2. Buscar alimentos")
        print("3. Eliminar alimentos")
        print("4. Editar alimento")
        print("5. Imprimir Inventario")
        opcion = int(input(">> "))

        if opcion == 1:
            numero_item = opcion_ingresar_alimentos(alimentos, precios, cantidades, numero_item, MAXIMO_INVENTARIO)
            guardar_alimentos(alimentos, "alimentos.txt", numero_item)
            guardar_precios(precios, "precios.txt", numero_item)
            guardar_cantidades(cantidades, "cantidades.txt", numero_item)
        elif opcion == 2:
            opcion_buscar_alimento(alimentos, precios, cantidades, numero_item)
        elif opcion == 3:
            numero_item = eliminar_alimento(alimentos, precios, cantidades, numero_item)
            guardar_alimentos(alimentos, "alimentos.txt", numero_item)
            guardar_precios(precios, "precios.txt", numero_item)
            guardar_cantidades(cantidades, "cantidades.txt", numero_item)
        elif opcion == 4:
            editar_alimento(alimentos, precios, cantidades, numero_item)
            guardar_alimentos(alimentos, "alimentos.txt", numero_item)
            guardar_precios(precios, "precios.txt", numero_item)
            guardar_cantidades(cantidades, "cantidades.txt", numero_item)
        elif opcion == 5:
            imprimir_alimentos(alimentos, precios, cantidades, numero_item)
        else:
            print("Opción no válida")

        opcionr = int(input("¿Desea elegir una nueva opción? 1.Sí / 2.No\n>> "))
        if opcionr != 1:
            break

if __name__ == "__main__":
    main()
