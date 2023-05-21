# Polymorphism is a core concept in object-oriented programming (OOP) 
# that allows objects of different classes to be treated as objects 
# of a common superclass. It enables the same code to be used with 
# different types of objects, providing flexibility and extensibility 
# in software design.

# Polymorphism involves the following key ideas:

# Inheritance: Polymorphism relies on inheritance to create a hierarchical 
# relationship between classes. By defining a common superclass and deriving 
# multiple subclasses from it, polymorphism allows objects of these subclasses 
# to be treated as instances of the superclass.

Method Overriding: Polymorphism is often achieved through method overriding. Subclasses can override methods inherited from the superclass, providing their own implementation while keeping the method signature (name and parameters) the same. This allows different subclasses to have specialized behavior for the same method.

# Method Invocation: Polymorphism enables objects of different classes to be 
# invoked using the same method name. The actual behavior of the method is determined dynamically at runtime based on the actual type of the object being referenced.

# Interface Compatibility: Polymorphism requires that the objects involved 
# exhibit interface compatibility. This means that they share a common set of 
# methods or behaviors defined in a common superclass or interface. The code 
# that interacts with these objects can use the methods defined in the common 
# interface, regardless of the specific type of object.

# The key benefit of polymorphism is that it allows for code reuse, extensibility, 
# and flexibility. It promotes modular and flexible designs by allowing different 
# classes to conform to a common interface and be used interchangeably where the 
# common interface is expected.



import turtle



class Polygon:
    def __init__(self, sides, name, size=100, color="black", line_thickness=1):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides - 2) * 180
        self.angle = self.interior_angles / self.sides
    

    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)

        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)


# Below example instance of Polymorphism examples

# square = Polygon(4, 'Square')
# pentagon = Polygon(5, 'Pentagon')
# hexagon = Polygon(6, 'Hexagon', 50, 'Red', line_thickness=5)

# square.draw()
# pentagon.draw()
# hexagon.draw()


# The blow example is Inheritance and Polymorphism

class Square(Polygon):
    # Constructor of Square
    def __init__(self, size=100, color="black", line_thickness=1):
        # Constructure of inherited class/parent class/super class
        super().__init__(4, "Square", size, color, line_thickness)
    

    def draw(self):
        turtle.begin_fill()
        # Parent class's method
        super().draw()
        turtle.end_fill()



square = Square(color='green', line_thickness=3)

print(f"Side: {square.sides}, Angle: {square.angle}")
square.draw()
# turtle.done()



class Pentagon(Polygon):
    # Constructor of Pentagon
    def __init__(self, size=100, color="black", line_thickness=1):
        super().__init__(5, "Pentagon", size, color, line_thickness)
    

    def draw(self):
        turtle.begin_fill()
        # Parent class's method
        super().draw()
        turtle.end_fill()


pentagon = Pentagon(color='blue', line_thickness=3)

print(f"Side: {pentagon.sides}, Angle: {pentagon.angle}")
pentagon.draw()
turtle.done()