# Design a simple class hierarchy to model geometric shapes, focusing on the concept of inheritance and method overriding. Start by creating a base class named Shape, which includes a method area() intended to be overridden by its subclasses. Then, develop two subclasses: Square and Triangle. The Square class should have a single attribute, side, and an overridden area() method that calculates and returns the square's area. Similarly, the Triangle class will have two attributes, base and height, with its area() method overridden to compute and return the triangle's area. Create a square oject and a triangle object and print their area.

# Input
# None

# Process
# Create parent Shape class
# create class that mutates original class methods

# Output
# square obj
# triangle obj


class Shape:
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


obj_square = Square(3)
obj_triangle = Triangle(3, 6)

print(obj_square.area())
print(obj_triangle.area())
