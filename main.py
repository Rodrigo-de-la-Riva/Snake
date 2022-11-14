import random
import pygame.display
from ajustes import *
from snake import Snake
from cube import Cube
from time import time
from lista_puntuacion import SimplyLinkedList
from pygame import *
from ajustes.settings import set_font

# Se crean las variables necesarias antes de iniciar el juego
punteo = SimplyLinkedList()
snake = Snake()
run = False
velocidad = FPS
dificult = ''
lista_size = 0
nombre = ''


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
            # Verifica la dificultad para que la comida no se genere sobre los obstaculos
            if dificult == 'Mid':
                if (dir_x, dir_y) == obstacle1.pos:
                    continue
                elif (dir_x, dir_y) == obstacle2.pos:
                    continue
                elif (dir_x, dir_y) == obstacle3.pos or (dir_x, dir_y) == obstacle3_1.pos \
                        or (dir_x, dir_y) == obstacle3_2.pos or (dir_x, dir_y) == obstacle3_3.pos:
                    continue
            elif dificult == 'Hard' or dificult == 'Dinamic':
                if (dir_x, dir_y) == obstacle1.pos:
                    continue
                elif (dir_x, dir_y) == obstacle2.pos:
                    continue
                elif (dir_x, dir_y) == obstacle3.pos or (dir_x, dir_y) == obstacle3_1.pos \
                        or (dir_x, dir_y) == obstacle3_2.pos or (dir_x, dir_y) == obstacle3_3.pos:
                    continue
                elif (dir_x, dir_y) == obstacle4.pos or (dir_x, dir_y) == obstacle4_1.pos \
                        or (dir_x, dir_y) == obstacle4_2.pos or (dir_x, dir_y) == obstacle4_3.pos:
                    continue
                elif (dir_x, dir_y) == obstacle5.pos or (dir_x, dir_y) == obstacle5_1.pos \
                        or (dir_x, dir_y) == obstacle5_2.pos or (dir_x, dir_y) == obstacle5_3.pos \
                        or (dir_x, dir_y) == obstacle5_4.pos or (dir_x, dir_y) == obstacle5_5.pos:
                    continue
            else:
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
def draw_game(surface, grid):
    win.fill(BG_COLOR)
    draw_grid(surface, grid)
    snake.draw(surface)
    food.draw(surface)

    # Verifica la dificultad para dibujar los obstaculos necesarios
    if dificult == 'Mid':
        obstacle1.draw(surface)
        obstacle2.draw(surface)
        obstacle3.draw(surface)
        obstacle3_1.draw(surface)
        obstacle3_2.draw(surface)
        obstacle3_3.draw(surface)

    elif dificult == 'Hard' or dificult == 'Dinamic':
        obstacle1.draw(surface)
        obstacle2.draw(surface)
        obstacle3.draw(surface)
        obstacle3_1.draw(surface)
        obstacle3_2.draw(surface)
        obstacle3_3.draw(surface)
        obstacle4.draw(surface)
        obstacle4_1.draw(surface)
        obstacle4_2.draw(surface)
        obstacle4_3.draw(surface)
        obstacle5.draw(surface)
        obstacle5_1.draw(surface)
        obstacle5_2.draw(surface)
        obstacle5_3.draw(surface)
        obstacle5_4.draw(surface)
        obstacle5_5.draw(surface)
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


# Funcion para definir el tamaño del texto
def font_size(size):
    font = set_font(size)
    return font


text1 = Rect(100, 25, 300, 50)
jugar = Rect(100, 100, 300, 50)
puntos = Rect(100, 200, 300, 50)
salir = Rect(100, 300, 300, 50)


def draw_button(boton, text, surface, color=WHITE, text_color=BLACK, size=30):
    pygame.init()
    pygame.font.init()
    draw.rect(surface, color, boton, 0)
    text = font_size(size).render(text, True, text_color)
    win.blit(text, (boton.x + (boton.width - text.get_width()) / 2, boton.y + (boton.height - text.get_height()) / 2))


# Funcion para el menu principal
def main_menu():
    global run, velocidad, win, dificult, snake
    run = False
    run_menu = True
    velocidad = FPS
    dificult = 'Easy'

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    win.fill(GREEN)
    while run_menu is True:
        draw_button(text1, 'Snake', win, color=GREEN)
        draw_button(jugar, 'Jugar', win)
        draw_button(puntos, 'Lista de puntuaciones', win)
        draw_button(salir, 'Salir', win)
        display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if jugar.collidepoint(mouse.get_pos()):
                    name_menu()
                if puntos.collidepoint(mouse.get_pos()):
                    score_menu()
                if salir.collidepoint(mouse.get_pos()):
                    print('Que tenga un buen dia')
                    run_menu = False

    pygame.quit()


text8 = Rect(100, 100, 300, 50)
ok = Rect(125, 250, 250, 50)
player_name = Rect(50, 150, 400, 50)


# Funcion para el menu para ingresar el nombre
def name_menu():
    global nombre
    run_menu = True
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    win.fill(WHITE)
    while run_menu is True:
        draw_button(text8, 'Ingrese su nombre', win)
        draw_button(ok, 'Aceptar', win, color=GREEN)
        draw_button(player_name, nombre, win, color=GREEN)
        display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += e.unicode

            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if ok.collidepoint(mouse.get_pos()):
                    color_menu()


text5 = Rect(100, 25, 300, 50)
text6 = Rect(0, 200, 500, 50)
text7 = Rect(50, 350, 400, 50)
p1 = Rect(0, 100, 500, 50)
p2 = Rect(0, 150, 500, 50)
p3 = Rect(0, 200, 500, 50)
p4 = Rect(0, 250, 500, 50)
p5 = Rect(0, 300, 500, 50)


# Menu para las puntuaciones
def score_menu():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    win.fill(GREEN)
    run_menu = True
    while run_menu is True:
        draw_button(text5, 'Tabla de posiciones', win, color=GREEN)
        if lista_size == 0:
            draw_button(text6, 'La tabla de puntuaciones esta vacia', win)
        elif lista_size == 1:
            draw_button(p1, punteo.positions(0), win, size=15)
        elif lista_size == 2:
            draw_button(p1, punteo.positions(0), win, size=15)
            draw_button(p2, punteo.positions(1), win, size=15)
        elif lista_size == 3:
            draw_button(p1, punteo.positions(0), win, size=15)
            draw_button(p2, punteo.positions(1), win, size=15)
            draw_button(p3, punteo.positions(2), win, size=15)
        elif lista_size == 4:
            draw_button(p1, punteo.positions(0), win, size=15)
            draw_button(p2, punteo.positions(1), win, size=15)
            draw_button(p3, punteo.positions(2), win, size=15)
            draw_button(p4, punteo.positions(3), win, size=15)
        elif lista_size == 5:
            draw_button(p1, punteo.positions(0), win, size=15)
            draw_button(p2, punteo.positions(1), win, size=15)
            draw_button(p3, punteo.positions(2), win, size=15)
            draw_button(p4, punteo.positions(3), win, size=15)
            draw_button(p5, punteo.positions(4), win, size=15)

        draw_button(text7, 'Volver al menu principal', win)
        display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if text7.collidepoint(mouse.get_pos()):
                    main_menu()


text2 = Rect(100, 25, 300, 50)
color1 = Rect(100, 100, 300, 50)
color2 = Rect(100, 200, 300, 50)
color3 = Rect(100, 300, 300, 50)
color4 = Rect(100, 400, 300, 50)


# Menu para los colores
def color_menu():
    global snake
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    win.fill(WHITE)
    run_menu = True

    while run_menu is True:
        draw_button(text2, 'Seleccion de color', win, color=WHITE)
        draw_button(color1, 'Rojo', win, color=RED)
        draw_button(color2, 'Azul', win, color=BLUE)
        draw_button(color3, 'Verde', win, color=GREEN)
        draw_button(color4, 'Aleatorio', win, color=WHITE)
        display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if color1.collidepoint(mouse.get_pos()):
                    snake = Snake(color=RED)
                    dificult_select()
                if color2.collidepoint(mouse.get_pos()):
                    snake = Snake(color=BLUE)
                    dificult_select()
                if color3.collidepoint(mouse.get_pos()):
                    snake = Snake(color=GREEN)
                    dificult_select()
                if color4.collidepoint(mouse.get_pos()):
                    snake = Snake(color=color_select())
                    dificult_select()


text3 = Rect(100, 25, 300, 50)
dif1 = Rect(100, 100, 300, 50)
dif2 = Rect(100, 200, 300, 50)
dif3 = Rect(100, 300, 300, 50)
dif4 = Rect(100, 400, 300, 50)


# Funcion para el menu de las dificultades
def dificult_select():
    global snake, dificult, velocidad, obstacle1, obstacle2, obstacle3, obstacle3_1, obstacle3_2, \
        obstacle3_3, obstacle4, obstacle4_1, obstacle4_2, obstacle4_3, obstacle5, obstacle5_1, obstacle5_2, \
        obstacle5_3, obstacle5_4, obstacle5_5, timer_start
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    win.fill(GREEN)
    run_menu = True

    while run_menu is True:
        draw_button(text3, 'Seleccion de dificultad', win, color=GREEN)
        draw_button(dif1, 'Facil', win, color=PINK)
        draw_button(dif2, 'Medio', win, color=BLUE)
        draw_button(dif3, 'Dificil', win, color=RED)
        draw_button(dif4, 'Dinamico', win, color=WHITE)
        display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if dif1.collidepoint(mouse.get_pos()):
                    snake.add_cube()
                    dificult = 'Easy'
                    game_start()
                if dif2.collidepoint(mouse.get_pos()):
                    snake.add_cube()

                    velocidad = velocidad * 2

                    # Variables para los obstaculos
                    obstacle1 = brick()
                    obstacle2 = brick()
                    obstacle3 = column()
                    obstacle3_1 = Cube((obstacle3.pos[0] - 1, obstacle3.pos[1]), color=BLACK)
                    obstacle3_2 = Cube((obstacle3_1.pos[0] - 1, obstacle3_1.pos[1]), color=BLACK)
                    obstacle3_3 = Cube((obstacle3_2.pos[0] - 1, obstacle3_2.pos[1]), color=BLACK)

                    dificult = 'Mid'
                    game_start()
                if dif3.collidepoint(mouse.get_pos()):
                    snake.add_cube()

                    velocidad = velocidad * 5

                    # Variables para los obstaculos
                    obstacle1 = brick()
                    obstacle2 = brick()
                    obstacle3 = column()
                    obstacle3_1 = Cube((obstacle3.pos[0] - 1, obstacle3.pos[1]), color=BLACK)
                    obstacle3_2 = Cube((obstacle3_1.pos[0] - 1, obstacle3_1.pos[1]), color=BLACK)
                    obstacle3_3 = Cube((obstacle3_2.pos[0] - 1, obstacle3_2.pos[1]), color=BLACK)
                    obstacle4 = column()
                    obstacle4_1 = Cube((obstacle4.pos[0] - 1, obstacle4.pos[1]), color=BLACK)
                    obstacle4_2 = Cube((obstacle4_1.pos[0] - 1, obstacle4_1.pos[1]), color=BLACK)
                    obstacle4_3 = Cube((obstacle4_2.pos[0] - 1, obstacle4_2.pos[1]), color=BLACK)
                    obstacle5 = wall()
                    obstacle5_1 = Cube((obstacle5.pos[0], obstacle5.pos[1] - 1), color=BLACK)
                    obstacle5_2 = Cube((obstacle5_1.pos[0], obstacle5_1.pos[1] - 1), color=BLACK)
                    obstacle5_3 = Cube((obstacle5_2.pos[0], obstacle5_2.pos[1] - 1), color=BLACK)
                    obstacle5_4 = Cube((obstacle5_3.pos[0], obstacle5_3.pos[1] - 1), color=BLACK)
                    obstacle5_5 = Cube((obstacle5_4.pos[0], obstacle5_4.pos[1] - 1), color=BLACK)

                    dificult = 'Hard'
                    game_start()
                if dif4.collidepoint(mouse.get_pos()):
                    snake.add_cube()

                    # Variables para los obstaculos
                    obstacle1 = brick()
                    obstacle2 = brick()
                    obstacle3 = column()
                    obstacle3_1 = Cube((obstacle3.pos[0] - 1, obstacle3.pos[1]), color=BLACK)
                    obstacle3_2 = Cube((obstacle3_1.pos[0] - 1, obstacle3_1.pos[1]), color=BLACK)
                    obstacle3_3 = Cube((obstacle3_2.pos[0] - 1, obstacle3_2.pos[1]), color=BLACK)
                    obstacle4 = column()
                    obstacle4_1 = Cube((obstacle4.pos[0] - 1, obstacle4.pos[1]), color=BLACK)
                    obstacle4_2 = Cube((obstacle4_1.pos[0] - 1, obstacle4_1.pos[1]), color=BLACK)
                    obstacle4_3 = Cube((obstacle4_2.pos[0] - 1, obstacle4_2.pos[1]), color=BLACK)
                    obstacle5 = wall()
                    obstacle5_1 = Cube((obstacle5.pos[0], obstacle5.pos[1] - 1), color=BLACK)
                    obstacle5_2 = Cube((obstacle5_1.pos[0], obstacle5_1.pos[1] - 1), color=BLACK)
                    obstacle5_3 = Cube((obstacle5_2.pos[0], obstacle5_2.pos[1] - 1), color=BLACK)
                    obstacle5_4 = Cube((obstacle5_3.pos[0], obstacle5_3.pos[1] - 1), color=BLACK)
                    obstacle5_5 = Cube((obstacle5_4.pos[0], obstacle5_4.pos[1] - 1), color=BLACK)

                    dificult = 'Dinamic'
                    timer_start = time()
                    game_start()


# Funcion encargada de correr el juego
def game_start():
    global velocidad, dificult, run, win, food, obstacle1, obstacle2, obstacle3, obstacle3_1, obstacle3_2, \
        obstacle3_3, obstacle4, obstacle4_1, obstacle4_2, obstacle4_3, obstacle5, obstacle5_1, obstacle5_2, \
        obstacle5_3, obstacle5_4, obstacle5_5, snake, timer_start
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    food_eaten = 0
    longitud = 1
    run = True

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

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
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

                    game_over()

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

                    game_over()

        # Verificar si aun tiene cuerpo la serpiente
        if snake.snake_len <= 1:
            print('Frutas comidas: ', food_eaten)
            score = food_eaten
            punteo.insert_by(score, nombre, longitud)

            snake.restart((10, 10))

            game_over()

        # Verificar choques con los obstaculos
        if dificult == 'Mid':
            if snake.cabeza.pos == obstacle1.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))

                game_over()

            elif snake.cabeza.pos == obstacle2.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))

                game_over()

            elif snake.cabeza.pos == obstacle3.pos or snake.cabeza.pos == obstacle3_1.pos \
                    or snake.cabeza.pos == obstacle3_2.pos or snake.cabeza.pos == obstacle3_3.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                game_over()

        # Verificar choques con los obstaculos
        elif dificult == 'Hard' or dificult == 'Dinamic':

            if snake.cabeza.pos == obstacle1.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                game_over()

            elif snake.cabeza.pos == obstacle2.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                game_over()

            elif snake.cabeza.pos == obstacle3.pos or snake.cabeza.pos == obstacle3_1.pos \
                    or snake.cabeza.pos == obstacle3_2.pos or snake.cabeza.pos == obstacle3_3.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                game_over()

            elif snake.cabeza.pos == obstacle4.pos or snake.cabeza.pos == obstacle4_1.pos \
                    or snake.cabeza.pos == obstacle4_2.pos or snake.cabeza.pos == obstacle4_3.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                game_over()

            elif snake.cabeza.pos == obstacle5.pos or snake.cabeza.pos == obstacle5_1.pos \
                    or snake.cabeza.pos == obstacle5_2.pos or snake.cabeza.pos == obstacle5_3.pos \
                    or snake.cabeza.pos == obstacle5_4.pos or snake.cabeza.pos == obstacle5_5.pos:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                game_over()

        draw_game(win, grid)

        # Verificar si la serpiente choco con ella misma
        try:
            choque = snake.positions_check()
            if choque is False:
                print('Frutas comidas: ', food_eaten)
                score = food_eaten
                punteo.insert_by(score, nombre, longitud)

                snake.restart((10, 10))
                run = False
                game_over()
        except AttributeError:
            pass


text4 = Rect(100, 100, 300, 100)
volver = Rect(100, 350, 300, 50)


def game_over():
    global lista_size
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    win.fill(BLACK)
    lista_size += 1
    run_menu = True

    while run_menu is True:
        draw_button(text4, 'GAME OVER', win, color=BLACK, text_color=RED)
        draw_button(volver, 'Volver al menu', win, color=WHITE)
        display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if volver.collidepoint(mouse.get_pos()):
                    main_menu()


main_menu()
