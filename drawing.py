import pygame

import level

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

background_image = pygame.image.load('sprites/background.jpg')
rocket_image = pygame.image.load('sprites/spaceship.png')


def draw_items(_level, surface: pygame.display):
    surface.blit(background_image, (0, 0))
    rocket_coords = _level.rocket.get_coordinates()
    surface.blit(rocket_image, rocket_coords)
    pygame.display.flip()