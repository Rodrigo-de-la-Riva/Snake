from node import Node


class SimplyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None and self.tail is None

    # insertar al inicio
    def unshift(self, data, name):
        new_node = Node(data, name=name)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    # insertar al final
    def appen(self, data, name):
        new_node = Node(data, name=name)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    # insertar en una posicion especifica
    def insert_at(self, data, pos, name):
        new_node = Node(data, name=name)
        if pos == 0:
            self.unshift(data, name)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            previous = self.find_at(pos - 1)
            new_node.next = previous.next
            previous.next = new_node
            self.size += 1

    # insertar mediante un dato especifico
    def insert_by(self, data, name):
        new_node = Node(data, name=name)
        pos = 0

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            if self.head.data <= data:
                self.unshift(data, name)
            elif self.tail.data >= data:
                self.appen(data, name)
            else:
                current = self.head
                while True:
                    if current.data <= data:
                        prev = self.find_at(pos - 1)
                        new_node.next = current
                        prev.next = new_node
                        break
                    current = current.next
                    pos += 1
                self.size += 1
        if self.size > 5:
            self.pop()

    # Encontrar mediante el valor deseado
    def find_by(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            else:
                current = current.next

        raise Exception('El elemento no existe')

    # Encontrar mediante la posicion deseada
    def find_at(self, pos):
        current = self.head
        i = 0
        while current is not None:
            if i == pos:
                return current
            else:
                current = current.next
                i += 1

        raise Exception('El elemento no existe')

    # Recorrer la lista
    def transversal(self):
        current = self.head
        result = ''
        while current is not None:
            result += f'{current.name}: {str(current.data)}'
            if current is not self.tail:
                result += '\n'
            current = current.next
        return result

    # Eliminar al final
    def pop(self):
        if self.is_empty():
            raise Exception('Subdesbordamiento de lista')
        elif self.size == 1:
            delete = self.head.data
            self.head = None
            self.tail = None
            self.size = 0

            return delete.data
        else:
            delete = self.tail
            prev = self.find_at(self.size - 2)
            self.tail = prev
            self.tail.next = None
            self.size -= 1

            return delete.data
