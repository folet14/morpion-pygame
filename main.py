import pygame
import pygame_textinput
from Grid import *
from Cell import *

#settings param
settings_size = (1920, 1080)
settings_bg_color = (225, 225, 225)
settings_ratio = (10, 50)

#game param
width = 1920
height = 1080
game_bg_color = (225, 225, 225)


def load_textures():
    textures = {
        "empty": pygame.image.load("pics/empty.png"),
        "cross": pygame.image.load("pics/cross.png"),
        "circle": pygame.image.load("pics/circle.png"),
        "settings": pygame.image.load("pics/settings.png"),
        "confirm": pygame.image.load("pics/confirm.png"),
        "restart": pygame.image.load("pics/restart.png"),
        "quit": pygame.image.load("pics/quit.png")
    }
    return textures


def is_good_value(entry, pos_value):
    if (pos_value == 0 and (3 <= entry <= 19)) or (pos_value == 1 and (3 <= entry <= 10)):
        return True
    return False


def is_good_settings(entry):
    if is_good_value(entry[0], 0) and is_good_value(entry[1], 1):
        return True
    return False


def settings():
    text_input = pygame_textinput.TextInput()
    screen = pygame.display.set_mode(settings_size)
    clock = pygame.time.Clock()
    entry = [0, 0]
    i = 0
    pygame.font.init()
    text_1 = "3 to 19"
    text_2 = "3 to 10"
    text_error = "wrong"
    font = pygame.font.Font(None, 24)
    text = font.render(text_1, 1, (000, 000, 000))
    while not(is_good_settings(entry)):
        screen.fill(settings_bg_color)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
        if text_input.update(events):
            try:
                entry[i] = int(text_input.get_text())
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
            print(entry)
            text_input.clear_text()
            if is_good_value(entry[i], i):
                i += 1
                text = font.render(text_2, 1, (000, 000, 000))
            else:
                text = font.render(text_error, 1, (000, 000, 000))
        screen.blit(text, (10, 10))
        screen.blit(text_input.get_surface(), settings_ratio)
        pygame.display.update()
        clock.tick(30)
    return entry


def initialisation():
    larg_haut = settings()
    return Grid(larg_haut[0], larg_haut[1])


textures = load_textures()
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.update()
grid = initialisation()
grid.draw_grid(display, textures)
