from cola_prioridad import ColaPrioridad
from nodo import nodo
from persona import Persona

def main():
    cola = ColaPrioridad()
    while True:
        print("\n--- Menú Cola de Prioridad ---")
        print("1. Llegada de persona")
        print("2. Atender persona")
        print("3. Mostrar cola")
        print("4. Salir")
        opcion = input("Seleccione: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido1 = input("Primer apellido: ")
            apellido2 = input("Segundo apellido: ")
            edad = int(input("Edad: "))
            p = Persona(nombre, apellido1, apellido2, edad)
            cola.insert(nodo(p))
            print("Persona agregada.")
        
        elif opcion == "2":
            print(cola.delete())
        
        elif opcion == "3":
            cola.imprimir()
        
        elif opcion == "4":
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()