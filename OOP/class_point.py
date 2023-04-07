import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Operator overloading
    def __add__(self, other):
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
        else:
            x = self.x + other
            y = self.y + other

        return Point(x, y)
        
    def plot(self):
        plt.scatter(self.x, self.y)

a = Point(1, 1)
b = Point(2, 2)
c = a + b
# d = Point(5, 5)
# c += d
d = a + 5

# print(c.x, c.y)
# c.plot()
d.plot()
# a.plot()
plt.show()
