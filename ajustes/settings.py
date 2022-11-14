import pygame
pygame.init()
pygame.font.init()

# Variables para los distintos colores del juego
RED = (250, 0, 0)
GREEN = (0, 250, 0)
BLUE = (0, 0, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (250, 0, 250)
DARK_YELLOW = (200, 150, 0)
YELLOW = (250, 250, 0)

BG_COLOR = WHITE

FPS = 10

# Variables de ancho, largo y columnas
WIDTH, HEIGHT = 500, 500
ROWS = COLS = 20

# Variables para el tamaño de los pixeles y para dibujar la cuadricula
PIXEL_SIZE = WIDTH // COLS
DRAW_GRID_LINES = True


def set_font(size):
    return pygame.font.SysFont('comicsans', size)
