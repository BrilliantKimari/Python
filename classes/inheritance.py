class Shape:


    def __init__(self,name):
        self.name=name

    def describe(self):
        print(f"This is a shape called {self.name}")



shape1=Shape(name="Circle")
shape1.describe()


class Circle(Shape):

    def __init__(self,radius):
        super().__init__(name="Circle")
        self.radius = radius

    def area(self):
        a = 3.142 * self.radius * self.radius
        print(f"The area of the circle is {a}")

c1 = Circle(radius=5)
c1.describe()
c1.area()


class Rectangle(Shape):

    def __init__(self,length,width):
        super().__init__(name="Rectangle")
        self.length = length
        self.width = width

    def area(self):
        a = self.length * self.width
        print(f"The area of the rectangle is {a}")

r1 = Rectangle(10,5)
r1.area()
r1.describe()

