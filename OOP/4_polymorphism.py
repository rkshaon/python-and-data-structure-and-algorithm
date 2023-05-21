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



# square = Polygon(4, 'Square')
# pentagon = Polygon(5, 'Pentagon')
# hexagon = Polygon(6, 'Hexagon', 50, 'Red', line_thickness=5)



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
turtle.done()