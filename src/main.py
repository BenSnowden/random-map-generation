from generateMap import make_world
from pygame.locals import *
import pygame
from time import sleep
from PIL import Image


dimension_of_screen = (1000, 800)

"""
dimension of map (x,y) used in map generation and setting the pygame screen size

"""


def init_display():

    global screen
    screen = pygame.display.set_mode(dimension_of_screen)


def run():
    """
    Logic to call functions to create and display the generated map

    """

    mapColored, worldValues, perlinNoise = make_world(dimension_of_screen)
    """
    Calls make_world(dimensions) to return
        mapColored = matrix of color values for each pixel which has been through 'add_color()'
        worldValues = matrix of light values for perlinNoise, not used currently
        perlinNoise = matrix that is grayscale, used to check if map generated properly visually.

    """

    init_display()
    Image.fromarray(perlinNoise, mode="L").show()
    Image.fromarray(mapColored, mode="RGB").show()

    mapColored = Image.fromarray(mapColored, mode="RGB")
    world = pygame.image.fromstring(
        mapColored.tobytes(),
        mapColored.size,
        mapColored.mode,
    )
    """
    world = use pillow to load colored map into a useable pygame format without having issues
    of distortion and an inversed x,y axis
    """

    screen.blit(world, (0, 0))
    pygame.display.update()

    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0

        pygame.display.update()
        sleep(1 / 10)


if __name__ == "__main__":
    run()
