import random
from ajustes import *
from snake import Snake
from cube import Cube


snake = Snake()

run = False
velocidad = FPS


# Funcion para el menu principal
def menu():
    global run, velocidad, win, food
    print('Bienvenido a Snake')
    print('1) Jugar')
    print('2) Ver Tabla de puntuaciones')
    print('3) Salir')
    opcion = int(input('Seleccione una opcion: '))
    if opcion == 1:
        print('Dificultad: ')
        print('1) Facil')
        print('2) Intermedio')
        print('3) Dificil')
        print('4) Dinamica')
        opcion = int(input('Seleccione la dificultad: '))
        if opcion == 1:
            win = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption('Snake')
            run = True
        elif opcion == 2:
            velocidad = velocidad * 2
            win = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption('Snake')
            run = True
        elif opcion == 3:
            velocidad = velocidad * 5
            win = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption('Snake')
            run = True
        elif opcion == 4:
            raise NotImplementedError
    elif opcion == 2:
        raise NotImplementedError
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
                food = food_type()

            elif food.food == 'pera':
                food = food_type()

            elif food.food == 'piña':
                food = food_type()

        draw(win, grid)

        try:
            for x in range(len(snake.body)):
                if snake.body[x].pos in list(map(lambda z: z.pos, snake.body[x + 1:])):
                    print('Puntos: ', len(snake.body))
                    snake.restart((10, 10))
                    run = False
        except IndexError:
            pygame.quit()
            input('Perdiste, presiona la tecla enter para volver al menu...')
            menu()


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

menu()
