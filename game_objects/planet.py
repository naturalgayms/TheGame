from game_objects.game_object import GameObject
from game_objects.human import Human
# from game_objects.rocket import Rocket
from program_variables import G, mass_of_rocket
import math


class Planet(GameObject):
    def __init__(self, x: int, y: int, radius: int, human: Human):
        super().__init__(x, y)
        self.radius = radius
        self.human = human
        self.gravity = G * (math.pi * self.radius * self.radius)

    def get_gravity(self, rocket):
        """
        Она дает обратный вектор, нужно возвращать с минусом
        :param rocket:
        :return:
        """
        f = (self.gravity * mass_of_rocket) / pow(self.get_distance_to_rocket(rocket), 2)
        cosx = (rocket.get_coordinates()[0] - self.get_coordinates()[0]) / self.get_distance_to_rocket(rocket)
        siny = (rocket.get_coordinates()[1] - self.get_coordinates()[1]) / self.get_distance_to_rocket(rocket)
        # if abs(rocket.x - self.x - self.radius / 2) < self.radius / 2 + 40 and \
        #         abs(rocket.y - self.y - self.radius / 2) < self.radius / 2 + 40:
        #     return 0, 0

        return -f * cosx, -f * siny  # вот здесь с минусом

    def get_human(self) -> Human:
        human = self.human
        self.human = None
        return human

    def get_human_angle_coordinate(self) -> float:
        human = self.human.get_coordinates()
        center = self.get_coordinates()
        dx = human[0] - center[0]
        dy = human[1] - center[1]
        return math.atan(dy / float(dx))

    def get_distance_to_rocket(self, rocket) -> float:
        planet = self.get_coordinates()
        rocket = rocket.get_coordinates()
        return math.sqrt((planet[0] - rocket[0]) * (planet[0] - rocket[0]) +
                         (planet[1] - rocket[1]) * (planet[1] - rocket[1]))
