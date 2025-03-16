from nodo_doble_enlace import nodo_doble

class lista_doble_ordenada:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def insert(self, new_node):
        nueva_edad = new_node.getData().edad

        # Caso: lista vacía
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
            return

        current = self.__head
        prev = None

        # Buscar posición ordenada por edad
        while current and current.getData().edad < nueva_edad:
            prev = current
            current = current.getNext()

        # Insertar al inicio
        if prev is None:
            new_node.setNext(self.__head)
            self.__head.setPrev(new_node)
            self.__head = new_node
        # Insertar al final
        elif current is None:
            self.__tail.setNext(new_node)
            new_node.setPrev(self.__tail)
            self.__tail = new_node
        # Insertar en medio
        else:
            prev.setNext(new_node)
            new_node.setPrev(prev)
            new_node.setNext(current)
            current.setPrev(new_node)

    def delete(self, pos):
        if self.__head is None:
            return "Lista vacía"

        current = self.__head
        index = 0

        # Buscar nodo en la posición
        while current and index != pos:
            current = current.getNext()
            index += 1

        if not current:
            return "Posición inválida"

        prev_node = current.getPrev()
        next_node = current.getNext()

        # Actualizar punteros
        if prev_node:
            prev_node.setNext(next_node)
        else:
            self.__head = next_node

        if next_node:
            next_node.setPrev(prev_node)
        else:
            self.__tail = prev_node

        return f"Borrado: {current.getData()}"

    def buscar_por_edad(self, edad):
        if self.__head is None:
            return []

        # Determinar inicio más cercano (cabeza o cola)
        diff_head = abs(self.__head.getData().edad - edad)
        diff_tail = abs(self.__tail.getData().edad - edad)
        current = self.__head if diff_head <= diff_tail else self.__tail
        resultados = []

        # Buscar desde el inicio elegido
        if current == self.__head:
            while current:
                if current.getData().edad == edad:
                    resultados.append(current.getData())
                current = current.getNext()
        else:
            while current:
                if current.getData().edad == edad:
                    resultados.append(current.getData())
                current = current.getPrev()

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
            print(f"{count}: {current.getData()}")
            current = current.getNext()
            count += 1
        print(f"Total: {count} personas")