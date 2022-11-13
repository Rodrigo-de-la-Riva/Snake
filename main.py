import random
from ajustes import *
from snake import Snake
from cube import Cube
from time import time
from lista_puntuacion import SimplyLinkedList

# Se crean las variables necesarias antes de iniciar el juego
punteo = SimplyLinkedList()
snake = Snake()
run = False
velocidad = FPS
dificult = ''


# Funcion para generar los obstaculos
def random_obsatcle(rows, item):
    positions = item.cabeza.pos

    # Se verifica que el obstaculo no se genere sobre la serpiente
    while True:
        dir_x = random.randrange(rows)
        dir_y = random.randrange(rows)
        if (dir_x, dir_y) == positions:
            continue
        else:
            break
    return dir_x, dir_y


# Funciones que generan los 3 tipos de obstaculos
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
    global obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, dificult
    positions = item.cabeza.pos

    while True:
        dir_x = random.randrange(rows)
        dir_y = random.randrange(rows)

        # Se verifica que la comida no se genere sobre la cabeza de la serpiente
        if (dir_x, dir_y) == positions:
            continue

        # Verifica la dificultad para que la comida no se genere sobre los obstaculos
        if dificult == 'Mid':
            if (dir_x, dir_y) == obstacle1.pos:
                continue
            elif (dir_x, dir_y) == obstacle2.pos:
                continue
            elif (dir_x, dir_y) == obstacle3.pos:
                continue
        elif dificult == 'Hard' or dificult == 'Dinamic':
            if (dir_x, dir_y) == obstacle1.pos:
                continue
            elif (dir_x, dir_y) == obstacle2.pos:
                continue
            elif (dir_x, dir_y) == obstacle3.pos:
                continue
            elif (dir_x, dir_y) == obstacle4.pos:
                continue
            elif (dir_x, dir_y) == obstacle5.pos:
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

    # Verifica la dificultad para dibujar los obstaculos necesarios
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


# Funcion de seleccion de color aleatorio
def color_select():
    color = ((random.randint(0, 250)), (random.randint(0, 250)), (random.randint(0, 250)))
    return color


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
    global run, velocidad, win, food, obstacle1, obstacle2, obstacle3, obstacle4, obstacle5, dificult, snake
    run = False
    nombre = ''
    longitud = 1
    velocidad = FPS
    dificult = 'Easy'
    food_eaten = 0
    timer_start = 0
    print('Bienvenido a Snake')
    print('1) Jugar')
    print('2) Tabla de puntuaciones')
    print('3) Salir')
    opcion = int(input('Seleccione una opcion: '))
    if opcion == 1:
        nombre = input('Ingrese su nombre: ')
        print('Seleccion de color para la serpiente')
        print('1) Rojo')
        print('2) Verde')
        print('3) Azul')
        print('4) Aleatorio')
        op = int(input('Seleccione el color: '))
        if op == 1:
            snake = Snake(color=RED)
        elif op == 2:
            snake = Snake(color=GREEN)
        elif op == 3:
            snake = Snake(color=BLUE)
        elif op == 4:
            snake = Snake(color=color_select())

        print('Dificultad: ')
        print('1) Facil')
        print('2) Intermedio')
        print('3) Dificil')
        print('4) Dinamica')
        opcion = int(input('Seleccione la dificultad: '))
        if opcion == 1:
            snake.add_cube()
            win = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption('Snake')
            dificult = 'Easy'
            run = True
        elif opcion == 2:
            snake.add_cube()

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
            snake.add_cube()

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
            snake.add_cube()

            win = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption('Snake')

            # Variables para los obstaculos
            obstacle1 = brick()
            obstacle2 = brick()
            obstacle3 = column()
            obstacle4 = column()
            obstacle5 = wall()

            dificult = 'Dinamic'
            timer_start = time()

            run = True

    elif opcion == 2:
        print('Tabla de puntuaciones: ')
        print(punteo.transversal())
        input('Pulse la tecla enter para continuar...')
        menu()
    elif opcion == 3:
        print('Que tenga un buen dia')

    # Ciclo encargado de correr el juego
    while run:
        if dificult != 'Dinamic':
            clock.tick(velocidad)
        else:
            clock.tick(velocidad)
            timer_end = time()
            if timer_end - timer_start >= 30:
                velocidad += 1
                timer_start = time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        snake.move()

        # Verificar si choca con la comida
        if snake.cabeza.pos == food.pos:
            if food.food == 'manzana':
                snake.add_cube()
                food = food_type()
                food_eaten += 1
                longitud += 1

            elif food.food == 'fresa':
                snake.add_cube()
                snake.add_cube()
                food = food_type()
                food_eaten += 1
                longitud += 2

            elif food.food == 'banano':
                snake.add_cube()
                snake.add_cube()
                snake.add_cube()
                food = food_type()
                food_eaten += 1
                longitud += 3

            elif food.food == 'pera':
                if snake.snake_len > 1:
                    snake.pop()
                    food = food_type()
                    food_eaten += 1
                    longitud -= 1
                else:
                    print('Frutas comidas: ', food_eaten)
                    score = food_eaten
                    punteo.insert_by(score, nombre, longitud)

                    food = food_type()

                    snake.restart((10, 10))

                    pygame.quit()
                    input('Perdiste, presiona la tecla enter para volver al menu...')
                    menu()
            elif food.food == 'piña':
                if snake.snake_len > 5:
                    snake.pop()
                    snake.pop()
                    snake.pop()
                    snake.pop()
                    snake.pop()

                    food = food_type()
                    food_eaten += 1
                    longitud -= 5

                else:
                    print('Frutas comidas: ', food_eaten)
                    score = food_eaten
                    punteo.insert_by(score, nombre, longitud)

                    food = food_type()

                    snake.restart((10, 10))

                    pygame.quit()
                    input('Perdiste, presiona la tecla enter para volver al menu...')
                    menu()

        # Verificar si aun tiene cuerpo la serpiente
        if snake.snake_len <= 1:
            print('Frutas comidas: ', food_eaten)
            score = food_eaten
            punteo.insert_by(score, nombre, longitud)

            snake.restart((10, 10))

            pygame.quit()
            input('Perdiste, presiona la tecla enter para volver al menu...')
            menu()

        # Verificar choques con los obstaculos
        if dificult == 'Mid':
            if snake.cabeza.pos == obstacle1.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))

                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
            elif snake.cabeza.pos == obstacle2.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))

                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
            elif snake.cabeza.pos == obstacle3.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()

        # Verificar choques con los obstaculos
        elif dificult == 'Hard' or dificult == 'Dinamic':

            if snake.cabeza.pos == obstacle1.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
            elif snake.cabeza.pos == obstacle2.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
            elif snake.cabeza.pos == obstacle3.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
            elif snake.cabeza.pos == obstacle4.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
            elif snake.cabeza.pos == obstacle5.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()

        draw(win, grid)

        # Verificar si la serpiente choco con ella misma
        try:
            choque = snake.positions_check()
            if choque is False:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                run = False
                pygame.quit()
                input('Perdiste, presiona la tecla enter para volver al menu...')
                menu()
        except AttributeError:
            pass


menu()
