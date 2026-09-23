import math 
class Vector2D:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x * other.x, self.y * other.y)
    def __remul__ (self, other: 'Vector2D') -> 'Vector2D':
        return self.__mul__

     
        