class nodo_doble:
    def __init__(self, data):
        self.__data = data  # Almacena un objeto de tipo Persona
        self.__next = None  # Puntero al siguiente nodo
        self.__prev = None  # Puntero al nodo anterior

    # Setters y Getters
    def setNext(self, next_node):
        self.__next = next_node

    def getNext(self):
        return self.__next

    def setPrev(self, prev_node):
        self.__prev = prev_node

    def getPrev(self):
        return self.__prev

    def getData(self):
        return self.__data

    # Representación en cadena del nodo
    def __str__(self):
        prev_data = self.__prev.getData() if self.__prev else None
        next_data = self.__next.getData() if self.__next else None
        return f"Data: {self.__data} | Prev: {prev_data} | Next: {next_data}"