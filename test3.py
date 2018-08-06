class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y )

    def temp(self):
        def temp1():
            return

        self.x = 1