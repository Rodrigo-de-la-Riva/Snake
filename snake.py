from cube import Cube
from ajustes import *


class Snake:
    # Lista que almacena los giros que realizo la serpiente
    turns = {}

    def __init__(self, pos_x=10, pos_y=10, color=GREEN):
        # Variables de la serpiente
        self.head = None
        self.tail = None
        self.snake_len = 0
        self.color = color
        self.cabeza = Cube((pos_x, pos_y), color=self.color)
        self.body = self.transversal()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dir_x = 0
        self.dir_y = 1
        self.insert(self.cabeza)

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
        for i in range(0, 1):
            p = self.cabeza.pos
            if p in self.turns:
                turn = self.turns[p]
                self.cabeza.move(turn[0], turn[1])
                if i == 1-1:
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

        # Actualiza la posicion del cuerpo de la serpiente
        current = self.head
        pos1 = current.pos
        while current.next is not None:
            pos2 = current.next.pos
            current = current.next
            current.pos = pos1
            pos1 = pos2

    # Funcion para dibujar la serpiente
    def draw(self, surface):
        current = self.head
        while current is not None:
            if current.pos == self.cabeza.pos:
                current.draw(surface, True)
            else:
                current.draw(surface)
            current = current.next

    # Funcion para añadir otro cubo al cuerpo de la serpiente
    def add_cube(self):
        current = self.head
        tail = self.cabeza
        dx, dy = tail.dir_x, tail.dir_y

        if dx == 1 and dy == 0:
            self.insert(Cube((tail.pos[0]-1, tail.pos[1]), color=self.color))
        elif dx == -1 and dy == 0:
            self.insert(Cube((tail.pos[0]+1, tail.pos[1]), color=self.color))
        elif dx == 0 and dy == 1:
            self.insert(Cube((tail.pos[0], tail.pos[1]-1), color=self.color))
        elif dx == 0 and dy == -1:
            self.insert(Cube((tail.pos[0], tail.pos[1]+1), color=self.color))

        while current is not None:
            current.dir_x = dx
            current.dir_y = dy
            current = current.next

    # Funcion que verifica si la cabeza choco con el cuerpo
    def positions_check(self):
        current = self.head.next
        while current.next is not None:
            if self.head.pos == current.next.pos:
                return False
            else:
                current = current.next

    # Funcion para reiniciar la serpiente a su posicion inicial
    def restart(self, pos):
        self.cabeza = Cube(pos, color=self.color)
        self.body = self.transversal()
        self.turns = {}
        self.dir_x = 0
        self.dir_y = 1
        self.head = None
        self.tail = None
        self.insert(self.cabeza)

    # Funciones para el funcionamiento de la cola
    def is_empty(self):
        return self.head is None and self.tail is None

    def insert(self, data):
        new_node = data
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.snake_len += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.snake_len += 1

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
        elif self.snake_len == 1:
            delete = self.head
            self.head = None
            self.tail = None
            self.snake_len = 0

            return delete
        else:
            delete = self.tail
            prev = self.find_at(self.snake_len - 2)
            self.tail = prev
            self.tail.next = None
            self.snake_len -= 1

            return delete
