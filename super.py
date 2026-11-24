# super() = Function used in a child class to call methods from a parent class(superclass)
#           Allows you to extend the functionality of the inherited methods

# without super we have something like this:
# class Circle:
#     def __init__(self, color, filled, radius):
#         self.color = color
#         self.filled = filled
#         self.radius = radius
        

# class Square:
#     def __init__(self, color, filled, width):
#         self.color = color
#         self.filled = filled
#         self.width = width
        


# class Triangle:
#      def __init__(self, color, filled, width, height):
#         self.color = color
#         self.filled = filled
#         self.width = width
#         self.height = height

# however in programming we tend not to repeat ourselves so we use super()


class Shape:
    def __init__(self, color, filled):
          self.color = color
          self.filled = filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self): # this is called method overriding becaus if a child class has the same method as the parent class, the child class method will override the parent class method
            print(f"It is a circle with an area of {3.14 * self.radius ** 2}cm^2")
        

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width ** 2}cm^2")


class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {0.5 * self.width * self.height}cm^2")


circle = Circle(color = "red", filled = True, radius= 5) # use keyword arguments to make it readable
square = Square(color = "blue", filled=False, width=6)
triangle = Triangle(color="green", filled=True, width=7, height= 8)
print(circle.color)
print(f'Circle_radius: {circle.radius}cm')
circle.describe()


print(square.color)
print(f'Square_width: {square.width}cm')
square.describe()

print(triangle.color)
print(f'Triangle_width: {triangle.width}cm')
print(f'Triangle_Height: {triangle.height}cm')
triangle.describe()