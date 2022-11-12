from cube import Cube
from ajustes import *


class Snake:
    # Variables de la serpiente (NO TIENEN NADA RELACIONADO CON LA PILA)
    turns = {}

    def __init__(self, pos_x=10, pos_y=10, color=GREEN):
        # Variables de la serpiente para la pila
        self.size = 0
        self.head = None
        self.tail = None

        # Variables de la serpiente (NO TIENEN NADA RELACIONADO CON LA PILA)
        self.color = color
        self.cabeza = Cube((pos_x, pos_y))
        self.body = self.transversal()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dir_x = 0
        self.dir_y = 1

    # Funcion para el movimiento de la serpiente
    def move(self):
        # Esta variable almacena la tecla presionada
        keys = pygame.key.get_pressed()

        # En este ciclo se revisa si la tecla presionada es una de las asignadas para el movimiento
        for key in keys:
            if keys[pygame.K_LEFT]:
                self.dir_x = -1
                self.dir_y = 0
                self.turns[self.cabeza.pos] = [self.dir_x, self.dir_y]

            elif keys[pygame.K_DOWN]:
                self.dir_x = 0
                self.dir_y = 1
                self.turns[self.cabeza.pos] = [self.dir_x, self.dir_y]

            elif keys[pygame.K_RIGHT]:
                self.dir_x = 1
                self.dir_y = 0
                self.turns[self.cabeza.pos] = [self.dir_x, self.dir_y]

            elif keys[pygame.K_UP]:
                self.dir_x = 0
                self.dir_y = -1
                self.turns[self.cabeza.pos] = [self.dir_x, self.dir_y]

        # Este ciclo controla los movimientos de la serpiente
        for i in range(self.size):
            p = self.cabeza.pos
            if p in self.turns:
                turn = self.turns[p]
                self.cabeza.move(turn[0], turn[1])
                if i == self.size-1:
                    self.turns.pop(p)
            else:
                if self.cabeza.dir_x == -1 and self.cabeza.pos[0] <= 0:
                    self.cabeza.pos = (self.cabeza.rows-1, self.cabeza.pos[1])
                elif self.cabeza.dir_x == 1 and self.cabeza.pos[0] >= self.cabeza.rows-1:
                    self.cabeza.pos = (0, self.cabeza.pos[1])
                elif self.cabeza.dir_y == -1 and self.cabeza.pos[1] <= 0:
                    self.cabeza.pos = (self.cabeza.pos[0], self.cabeza.rows-1)
                elif self.cabeza.dir_y == 1 and self.cabeza.pos[1] >= self.cabeza.rows-1:
                    self.cabeza.pos = (self.cabeza.pos[0], 0)
                else:
                    self.cabeza.move(self.cabeza.dir_x, self.cabeza.dir_y)

    # Funcion para dibujar la serpiente
    def draw(self, surface):
        for i in range(self.size):
            if i == 0:
                self.cabeza.draw(surface, True)
            else:
                self.tail.draw(surface)

    # Funcion para añadir otro cubo al cuerpo de la serpiente
    def add_cube(self):
        tail = self.cabeza
        dx, dy = tail.dir_x, tail.dir_y

        if dx == 1 and dy == 0:
            self.insert(Cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.insert(Cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.insert(Cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.insert(Cube((tail.pos[0], tail.pos[1]+1)))

        self.tail.dir_x = dx
        self.tail.dir_y = dy

    # Funcion para reiniciar la serpiente a su posicion inicial
    def restart(self, pos):
        self.cabeza = Cube(pos)
        self.body = self.transversal()
        self.turns = {}
        self.dir_x = 0
        self.dir_y = 1
        self.size = 0
        self.head = None
        self.tail = None

    # Funciones para el funcionamiento de la cola
    def is_empty(self):
        return self.head is None and self.tail is None

    def insert(self, data):
        new_node = data
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def transversal(self):
        current = self.head
        total = ''
        while current is not None:
            total += str(current)
            current = current.next
        return total

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

    def pop(self):
        if self.is_empty():
            raise Exception('Subdesbordamiento de lista')
        elif self.size == 1:
            delete = self.head
            self.head = None
            self.tail = None
            self.size = 0

            return delete
        else:
            delete = self.tail
            prev = self.find_at(self.size - 2)
            self.tail = prev
            self.tail.next = None
            self.size -= 1

            return delete
