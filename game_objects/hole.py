from game_objects.game_object import GameObject


class Hole(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)