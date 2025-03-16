from nodo import nodo

class lista_enlazada_ordenada:
    def __init__(self):
        self.__head = None

    def insert(self, new_node):
        current = self.__head
        prev = None
        nueva_edad = new_node.getData().edad

        # Encontrar posición ordenada
        while current and current.getData().edad < nueva_edad:
            prev = current
            current = current.getNext()

        # Insertar
        if prev is None:  # Al inicio
            new_node.setNext(self.__head)
            self.__head = new_node
        else:  # En medio o final
            prev.setNext(new_node)
            new_node.setNext(current)

    def delete(self, pos):
        if self.__head is None:
            return "Lista vacía"
        
        current = self.__head
        prev = None
        index = 0

        while current and index != pos:
            prev = current
            current = current.getNext()
            index += 1

        if not current:
            return "Posición inválida"
        
        if prev is None:
            self.__head = current.getNext()
        else:
            prev.setNext(current.getNext())

        return f"Borrado: {current.getData()}"

    def buscar_por_edad(self, edad):
        resultados = []
        current = self.__head
        while current:
            if current.getData().edad == edad:
                resultados.append(current.getData())
            current = current.getNext()
        return resultados

    def buscar_por_nombre(self, subcadena):
        resultados = []
        current = self.__head
        while current:
            if subcadena.lower() in current.getData().nombre.lower():
                resultados.append(current.getData())
            current = current.getNext()
        return resultados

    def buscar_por_apellido(self, subcadena):
        resultados = []
        current = self.__head
        while current:
            apellidos = f"{current.getData().apellido1} {current.getData().apellido2}"
            if subcadena.lower() in apellidos.lower():
                resultados.append(current.getData())
            current = current.getNext()
        return resultados

    def imprimir(self):
        current = self.__head
        count = 0
        while current:
            print(f"{count}: {current}")
            current = current.getNext()
            count += 1
        print(f"Total: {count} personas")