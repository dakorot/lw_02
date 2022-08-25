from __future__ import annotations


class Vector3:

    def __init__(self, x: float, y: float, z: float):
        for a in [x, y, z]:
            if not (isinstance(a, float) or isinstance(a, int)):
                raise TypeError("Coords must be numbers")
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other: Vector3) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def get_coords(self) -> (float, float, float):
        return self.x, self.y, self.z

    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

    def __add__(self, other: Vector3) -> Vector3:
        return Vector3(self.x + other.x,
                       self.y + other.y,
                       self.z + other.z)

    def __sub__(self, other: Vector3) -> Vector3:
        return Vector3(self.x - other.x,
                       self.y - other.y,
                       self.z - other.z)

    def __mul__(self, other: Vector3) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z
