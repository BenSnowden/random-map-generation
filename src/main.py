from generateMap import make_world
from pygame.locals import *
import pygame
from time import sleep
from PIL import Image
import numpy as np

dimension_of_screen = (1000, 800)


def init_display():
    global screen
    screen = pygame.display.set_mode(dimension_of_screen)


def run():
    image_colored, perlin_world, image_perlin_noise = make_world(dimension_of_screen)

    init_display()

    Image.fromarray(image_perlin_noise, mode="L").show()

    Image.fromarray(image_colored, mode="RGB").show()

    world_pillow_image = Image.fromarray(image_colored, mode="RGB")
    world = pygame.image.fromstring(
        world_pillow_image.tobytes(), world_pillow_image.size, world_pillow_image.mode
    )

    screen.blit(world, (0, 0))
    pygame.display.update()

    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0

        pygame.display.update()
        sleep(1 / 30)


if __name__ == "__main__":
    run()
