import random
from ajustes import *
from snake import Snake
from cube import Cube
from lista_puntuacion import SimplyLinkedList

snake = Snake()
punteo = SimplyLinkedList()
run = False
velocidad = FPS


# Funcion para generar los obstaculos
def random_obsatcle(rows, item):
    positions = item.body

    while True:
        dir_x = random.randrange(rows)
        dir_y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (dir_x, dir_y), positions))) > 0:
            continue
        else:
            break
    return dir_x, dir_y


def brick():
    ladrillo = Cube(random_obsatcle(ROWS, snake), color=BLACK)
    return ladrillo


def wall():
    pared = Cube(random_obsatcle(ROWS, snake), color=BLACK)
    return pared


def column():
    columna = Cube(random_obsatcle(ROWS, snake), color=BLACK)
    return columna


# Funcion para generar la comida
def random_food(rows, item):
    positions = item.body

    while True:
        dir_x = random.randrange(rows)
        dir_y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (dir_x, dir_y), positions))) > 0:
            continue
        else:
            break
    return dir_x, dir_y


def food_type():
    global food
    comida = random.randint(1, 100)
    if 1 <= comida <= 40:
        food = Cube(random_food(ROWS, snake), color=RED, food='manzana')

    elif 41 <= comida <= 65:
        food = Cube(random_food(ROWS, snake), color=PINK, food='fresa')

    elif 66 <= comida <= 85:
        food = Cube(random_food(ROWS, snake), color=DARK_YELLOW, food='banano')

    elif 86 <= comida <= 95:
        food = Cube(random_food(ROWS, snake), color=GREEN, food='pera')

    elif 96 <= comida <= 100:
        food = Cube(random_food(ROWS, snake), color=YELLOW, food='piña')

    return food


# Variable que almacenara la comida
food = food_type()


# Funciones de dibujo
def draw(surface, grid):
    win.fill(BG_COLOR)
    draw_grid(surface, grid)
    snake.draw(surface)
    food.draw(surface)
    if dificult == 'Mid':
        obstacle1.draw(surface)
        obstacle2.draw(surface)
        obstacle3.draw(surface)
    elif dificult == 'Hard' or dificult == 'Dinamic':
        obstacle1.draw(surface)
        obstacle2.draw(surface)
        obstacle3.draw(surface)
        obstacle4.draw(surface)
        obstacle5.draw(surface)
    pygame.display.update()


# Funciones de dibujo para la cuadricula
def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(color)

    return grid


def draw_grid(surface, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(surface, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS):
            pygame.draw.line(surface, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS):
            pygame.draw.line(surface, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT))


clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)


# Funcion para el menu principal
def menu():
    global run, velocidad, win, food, obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, dificult
    run = False
    nombre = ''
    velocidad = FPS
    dificult = 'Easy'
    print('Bienvenido a Snake')
    print('1) Jugar')
    print('2) Tabla de puntuaciones')
    print('3) Salir')
    opcion = int(input('Seleccione una opcion: '))
    if opcion == 1:
        nombre = input('Ingrese su nombre: ')
        print('Dificultad: ')
        print('1) Facil')
        print('2) Intermedio')
        print('3) Dificil')
        print('4) Dinamica')
        opcion = int(input('Seleccione la dificultad: '))
        if opcion == 1:
            win = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption('Snake')
            dificult = 'Easy'
            run = True
        elif opcion == 2:
            velocidad = velocidad * 2
            win = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption('Snake')

            # Variables para los obstaculos
            obstacle1 = brick()
            obstacle2 = brick()
            obstacle3 = column()

            dificult = 'Mid'

            run = True
        elif opcion == 3:
            velocidad = velocidad * 5
            win = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption('Snake')

            # Variables para los obstaculos
            obstacle1 = brick()
            obstacle2 = brick()
            obstacle3 = column()
            obstacle4 = column()
            obstacle5 = wall()

            dificult = 'Hard'

            run = True
        elif opcion == 4:

            # Variables para los obstaculos
            obstacle1 = brick()
            obstacle2 = brick()
            obstacle3 = column()
            obstacle4 = column()
            obstacle5 = wall()

            dificult = 'Dinamic'

    elif opcion == 2:
        print('Tabla de puntuaciones: ')
        print(punteo.transversal())
        input('Pulse la tecla enter para continuar...')
        menu()
    elif opcion == 3:
        print('Que tenga un buen dia')

    # Ciclo encargado de correr el juego
    while run:
        clock.tick(velocidad)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        snake.move()

        if snake.body[0].pos == food.pos:
            if food.food == 'manzana':
                snake.add_cube()
                food = food_type()

            elif food.food == 'fresa':
                snake.add_cube()
                snake.add_cube()
                food = food_type()

            elif food.food == 'banano':
                snake.add_cube()
                snake.add_cube()
                snake.add_cube()
                food = food_type()

            elif food.food == 'pera':
                food = food_type()

            elif food.food == 'piña':
                food = food_type()

        if dificult == 'Mid':
            if snake.body[0].pos == obstacle1.pos:
                print('Puntos: ', len(snake.body))
                score = len(snake.body)
                punteo.insert_by(score, name=nombre)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
            elif snake.body[0].pos == obstacle2.pos:
                print('Puntos: ', len(snake.body))
                score = len(snake.body)
                punteo.insert_by(score, name=nombre)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
            elif snake.body[0].pos == obstacle3.pos:
                print('Puntos: ', len(snake.body))
                score = len(snake.body)
                punteo.insert_by(score, name=nombre)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
        elif dificult == 'Hard' or dificult == 'Dinamic':
            if snake.body[0].pos == obstacle1.pos:
                print('Puntos: ', len(snake.body))
                score = len(snake.body)
                punteo.insert_by(score, name=nombre)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
            elif snake.body[0].pos == obstacle2.pos:
                print('Puntos: ', len(snake.body))
                score = len(snake.body)
                punteo.insert_by(score, name=nombre)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
            elif snake.body[0].pos == obstacle3.pos:
                print('Puntos: ', len(snake.body))
                score = len(snake.body)
                punteo.insert_by(score, name=nombre)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
            elif snake.body[0].pos == obstacle4.pos:
                print('Puntos: ', len(snake.body))
                score = len(snake.body)
                punteo.insert_by(score, name=nombre)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
            elif snake.body[0].pos == obstacle5.pos:
                print('Puntos: ', len(snake.body))
                score = len(snake.body)
                punteo.insert_by(score, name=nombre)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()

        draw(win, grid)

        try:
            for x in range(len(snake.body)):
                if snake.body[x].pos in list(map(lambda z: z.pos, snake.body[x + 1:])):
                    print('Puntos: ', len(snake.body))
                    score = len(snake.body)
                    punteo.insert_by(score, name=nombre)

                    snake.restart((10, 10))
                    run = False
        except IndexError:
            pygame.quit()
            input('Perdiste, presiona la tecla enter para volver al menu...')
            menu()


menu()
