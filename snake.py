from cube import Cube
from node import Node
from ajustes import *


class Snake:
    # Variables de la serpiente (NO TIENEN NADA RELACIONADO CON LA PILA)
    turns = {}
    body = []

    def __init__(self, pos_x=10, pos_y=10):
        # Variables de la serpiente para la pila
        self.size = 0
        self.head = None

        # Variables de la serpiente (NO TIENEN NADA RELACIONADO CON LA PILA)
        self.color = GREEN
        self.cabeza = Cube((pos_x, pos_y))
        self.body.append(self.cabeza)
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
                self.turns[self.cabeza.pos[:]] = [self.dir_x, self.dir_y]

            elif keys[pygame.K_DOWN]:
                self.dir_x = 0
                self.dir_y = 1
                self.turns[self.cabeza.pos[:]] = [self.dir_x, self.dir_y]

            elif keys[pygame.K_RIGHT]:
                self.dir_x = 1
                self.dir_y = 0
                self.turns[self.cabeza.pos[:]] = [self.dir_x, self.dir_y]

            elif keys[pygame.K_UP]:
                self.dir_x = 0
                self.dir_y = -1
                self.turns[self.cabeza.pos[:]] = [self.dir_x, self.dir_y]

        # Este ciclo hace que el cuerpo de la serpiente siga el movimiento de la cabeza
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dir_x == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dir_x == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0, c.pos[1])
                elif c.dir_y == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows-1)
                elif c.dir_y == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                else:
                    c.move(c.dir_x, c.dir_y)

    # Funcion para dibujar la serpiente
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dir_x, tail.dir_y

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1]+1)))

        self.body[-1].dir_x = dx
        self.body[-1].dir_y = dy

    # Funcion para reiniciar la serpiente a su posicion inicial
    def restart(self, pos):
        self.cabeza = Cube(pos)
        self.body = []
        self.body.append(self.cabeza)
        self.turns = {}
        self.dir_x = 0
        self.dir_y = 1

    # Funciones para el funcionamiento de la pila
    def is_empty(self):
        return self.head is None

    def insert(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def delete(self):
        if self.is_empty():
            raise Exception('Subdesbordamiento de pila')
        else:
            delete = self.head
            self.head = self.head.next
            delete.next = None
            self.size -= 1

    def transversal(self):
        current = self.head
        total = ''
        while current is not None:
            total += str(current.data)
            current = current.next
        return total
