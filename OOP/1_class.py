# In Python, a class is a blueprint for creating objects (instances) 
# that share similar attributes and behavior. It provides a way to 
# define and organize code in a structured manner, allowing you to 
# create reusable and modular code.

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, {self.name}!")

# Creating an instance of the class
obj1 = MyClass("Alice", 32)
obj2 = MyClass("Shaon", 24)

print(obj1.age)  # Output: 32
print(obj2.age)  # Output: 24

obj1.greet()  # Output: Hello, Alice!
obj2.greet()  # Output: Hello, Shaon!
