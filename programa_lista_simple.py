from lista_enlazada_ordenada import lista_enlazada_ordenada
from nodo import nodo
from persona import Persona

def menu_busqueda(lista):
    print("\n--- Buscar por ---")
    print("1. Edad")
    print("2. Nombre")
    print("3. Apellido")
    opcion = input("Seleccione: ")

    if opcion == "1":
        edad = int(input("Edad a buscar: "))
        resultados = lista.buscar_por_edad(edad)
    elif opcion == "2":
        sub = input("Subcadena en nombre: ")
        resultados = lista.buscar_por_nombre(sub)
    elif opcion == "3":
        sub = input("Subcadena en apellido: ")
        resultados = lista.buscar_por_apellido(sub)
    else:
        return

    if resultados:
        print("\nResultados:")
        for p in resultados:
            print(p)
    else:
        print("No hay coincidencias.")

def main():
    lista = lista_enlazada_ordenada()
    while True:
        print("\n--- Menú Lista Simple ---")
        print("1. Agregar persona")
        print("2. Listar personas")
        print("3. Borrar por posición")
        print("4. Buscar personas")
        print("5. Salir")
        opcion = input("Seleccione: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido1 = input("Primer apellido: ")
            apellido2 = input("Segundo apellido: ")
            edad = int(input("Edad: "))
            p = Persona(nombre, apellido1, apellido2, edad)
            lista.insert(nodo(p))
            print("Persona agregada.")
        
        elif opcion == "2":
            print("\nLista de personas:")
            lista.imprimir()

        elif opcion == "3":
            pos = int(input("Posición a borrar: "))
            print(lista.delete(pos))

        elif opcion == "4":
            menu_busqueda(lista)

        elif opcion == "5":
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()