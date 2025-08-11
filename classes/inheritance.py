class Shape:


    def __init__(self,name,radius):
        self.name=name

    def describe(self):
        print(f"This is a shape called {self.name}")

    def area(self):
        a = 3.142 * self.radius * self.radius
        print(f"The area of the {self.name} is {a}")


shape1=Shape(name="Circle",5)
shape1.area()
shape1.describe()


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

