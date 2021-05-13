import noise
import numpy as np


def make_world(dimension_of_screen):
    scale = 1
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0
    seed = np.random.randint(0, 100)

    world = np.zeros(dimension_of_screen)

    x_idx = np.linspace(0, 1, dimension_of_screen[0])
    y_idx = np.linspace(0, 1, dimension_of_screen[1])
    world_x, world_y = np.meshgrid(x_idx, y_idx)

    world = np.vectorize(noise.pnoise2)(
        world_x / scale,
        world_y / scale,
        octaves=octaves,
        persistence=persistence,
        lacunarity=lacunarity,
        repeatx=dimension_of_screen[0],
        repeaty=dimension_of_screen[1],
        base=seed,
    )

    img = np.floor((world + 0.5) * 255).astype(np.uint8)

    color_world = add_color(world, dimension_of_screen)
    img_color = np.floor((color_world)).astype(np.uint8)

    return img_color, world, img


def add_color(world, dimension_of_screen):
    water = [78, 188, 185]
    water_deep = [66, 172, 175]
    water_shallow = [159, 205, 208]
    grass = [177, 211, 84]
    grass_light = [195, 214, 87]
    grass_dark = [112, 204, 55]
    beach = [231, 213, 147]
    snow = [255, 250, 250]
    mountain = [205, 216, 215]

    color_world = np.zeros((dimension_of_screen[1], dimension_of_screen[0]) + (3,))
    print(world[799][999])
    print(len(world[0]))
    print(len(world))
    print(len(color_world[0]))
    print(len(color_world))

    for i in range(799):
        for j in range(999):
            if world[i][j] < -0.2:
                color_world[i][j] = water_deep
            elif world[i][j] < -0.06:
                color_world[i][j] = water
            elif world[i][j] < -0.005:
                color_world[i][j] = water_shallow
            elif world[i][j] < 0.01:
                color_world[i][j] = beach
            elif world[i][j] < 0.1:
                color_world[i][j] = grass_light
            elif world[i][j] < 0.2:
                color_world[i][j] = grass
            elif world[i][j] < 0.26:
                color_world[i][j] = grass_dark
            elif world[i][j] < 0.35:
                color_world[i][j] = mountain
            elif world[i][j] >= 0.35:
                color_world[i][j] = snow

    return color_world
