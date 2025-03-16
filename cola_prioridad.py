from nodo import nodo
from persona import Persona

class ColaPrioridad:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__ultimo_prioritario = None  # Último nodo con edad >= 65

    def insert(self, new_node):
        persona = new_node.getData()

        # Caso 1: Cola vacía
        if not self.__head:
            self.__head = new_node
            self.__tail = new_node
            if persona.edad >= 65:
                self.__ultimo_prioritario = new_node
            return

        # Caso 2: Persona con prioridad
        if persona.edad >= 65:
            if not self.__ultimo_prioritario:  # Insertar al inicio
                new_node.setNext(self.__head)
                self.__head = new_node
            else:  # Insertar después del último prioritario
                new_node.setNext(self.__ultimo_prioritario.getNext())
                self.__ultimo_prioritario.setNext(new_node)
            self.__ultimo_prioritario = new_node
        else:  # Insertar al final
            self.__tail.setNext(new_node)
            self.__tail = new_node

    def delete(self):
        if not self.__head:
            return "Cola vacía"
        
        eliminado = self.__head
        self.__head = self.__head.getNext()
        
        # Actualizar último prioritario si se elimina
        if eliminado == self.__ultimo_prioritario:
            self.__ultimo_prioritario = None
        
        return f"Atendido: {eliminado.getData()}"

    def imprimir(self):
        current = self.__head
        count = 0
        print("\n--- Estado de la cola ---")
        while current:
            print(f"{count}: {current.getData()}")
            current = current.getNext()
            count += 1
        print(f"Total: {count} personas\n")