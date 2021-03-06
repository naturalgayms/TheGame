import pygame
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

background_image = pygame.image.load('sprites/back.png')
rocket_image = pygame.image.load('sprites/spaceship0.png')
rocket_pics = [pygame.image.load('sprites/p1.png'),
               pygame.image.load('sprites/p2.png'),
               pygame.image.load('sprites/p3.png'),
               pygame.image.load('sprites/p4.png'),
               pygame.image.load('sprites/p5.png'),
               pygame.image.load('sprites/p6.png'),
               pygame.image.load('sprites/p7.png'),
               pygame.image.load('sprites/p8.png'),
               pygame.image.load('sprites/p9.png'),
               pygame.image.load('sprites/p10.png')
               ]
blackhole_image = pygame.image.load('sprites/blackhole.png')
earth_image = pygame.transform.scale(pygame.image.load('sprites/Terran1.png'), (170, 170))
asteroid_pic = pygame.transform.scale(pygame.image.load('sprites/asteroid.png'), (randint(40, 100), randint(40, 100)))
human_pic = pygame.image.load('sprites/chelik.png')
asteroid_pic_2 = pygame.transform.scale(pygame.image.load('sprites/as_2.png'), (randint(40, 100), randint(40, 100)))
asteroid_pic_3 = pygame.transform.scale(pygame.image.load('sprites/as_3.png'), (randint(40, 100), randint(40, 100)))


def draw_items(_level, surface: pygame.display):
    surface.blit(background_image, (0, 0))
    label = pygame.font.SysFont("monospace", 30).render(str(_level.score), 1, (255, 255, 0))
    surface.blit(label, (surface.get_width() - 60, 0))
    if _level.score == 0:
        if _level.is_last:
            surface.blit(earth_image, _level.hole.get_coordinates())
        else:
            surface.blit(blackhole_image, _level.hole.get_coordinates())
    SingleColorBar(surface, RED, 0, 0, _level.rocket.fuel)
    rocket_coords = _level.rocket.get_coordinates()
    rocket_angle = - _level.rocket.return_angle() * 57.32
    rocket_image_with_angle = rot_center(rocket_image, rocket_angle, rocket_coords)

    for planet in _level.planets:
        planet_pic = rocket_pics[(planet.x + planet.y) % 10]
        new_pic = pygame.transform.scale(planet_pic, (planet.radius * 2, planet.radius * 2))
        surface.blit(new_pic, (planet.x - planet.radius, planet.y - planet.radius))
        if planet.human:
            human_coords = planet.human.get_coordinates()
            human_image = pygame.transform.scale(human_pic, (25, 25))
            human_image = pygame.transform.rotate(human_image, planet.human.angle * 57.32)
            rect = human_image.get_rect()
            rect.move_ip(*human_coords)
            rot_rect = human_image.get_rect(center=rect.center)
            surface.blit(human_image, (rot_rect[0] - 12.5, rot_rect[1] - 12.5))
        # pygame.draw.circle(surface, 255, planet.get_coordinates(), planet.radius, 12)

        # draw_at_center(surface, new_pic, planet_rect)
    for asteroid in _level.asteroids:
        asteroid_rect = pygame.Rect(0, 0, *asteroid.get_coordinates())
        if asteroid.id == 1:
            draw_asteroid_at_center(surface, asteroid_pic, asteroid_rect)
        if asteroid.id == 2:
            draw_asteroid_at_center(surface, asteroid_pic_2, asteroid_rect)
        if asteroid.id == 3:
            draw_asteroid_at_center(surface, asteroid_pic_3, asteroid_rect)

    surface.blit(*rocket_image_with_angle)
    pygame.display.flip()


def rot_center(image, angle, rocket_coords):
    rot_image = pygame.transform.rotate(image, angle)
    rect = image.get_rect()
    rect.move_ip(*rocket_coords)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, (rot_rect[0] - 35, rot_rect[1] - 7.5)


def get_scaled_size(rect, ratio):
    return int(rect.height * ratio), int(rect.width * ratio)


from program_variables import GLOBAL_HEIGHT, GLOBAL_WIDTH


def get_color(xx):
    max = 1

    fromR = 255
    fromG = 0
    fromB = 0

    toR = 0
    toG = 255
    toB = 0

    deltaR = round((toR - fromR) / max)
    deltaG = round((toG - fromG) / max)
    deltaB = round((toB - fromB) / max)
    R = fromR + xx * deltaR
    G = fromG + xx * deltaG
    B = fromB + xx * deltaB

    return (R, G, B)


def SingleColorBar(surface, color, x, y, value):
    xx = value / 1000
    try:
        pygame.draw.rect(surface, get_color(xx), (x, y, xx * GLOBAL_WIDTH, 32), 0)
    except:
        pass


# def draw_at_center(surface, picture, rect):
#     surface.blit(picture, (rect.left - picture.get_width() // 2, rect.top - picture.get_height() // 2))


def draw_asteroid_at_center(surface, picture, rect):
    surface.blit(picture, (rect.width - picture.get_width() // 2, rect.height - picture.get_height() // 2))
