# Encapsulation is a fundamental principle in object-oriented programming (OOP) 
# that combines data and the methods (functions) that operate on that data into 
# a single unit called an object. It involves bundling the data and methods 
# together, and controlling access to them through a well-defined interface.

# Here are the key aspects of encapsulation:

# Data and Methods: Encapsulation allows you to group related 
# data (attributes or variables) and methods (functions or procedures) 
# into a cohesive entity, known as an object. The data represents the 
# state or properties of the object, while the methods define its 
# behavior or operations.

# Access Modifiers: Encapsulation uses access modifiers, such as 
# public, private, and protected, to control the visibility and 
# accessibility of the attributes and methods. These modifiers 
# specify who can access and modify the data and methods from 
# within and outside the object.

# Public: Public attributes and methods are accessible from 
# anywhere, both inside and outside the object. They form the 
# public interface or API (Application Programming Interface) 
# of the object, allowing other objects or code to interact 
# with it.

# Private: Private attributes and methods are only accessible within 
# the object itself. They cannot be accessed or modified directly 
# from outside the object. Private members are typically accessed 
# through public methods, which provide controlled and validated 
# access to the private data.

# Protected: Protected attributes and methods are similar to private 
# members but are also accessible within subclasses or derived classes. 
# They provide a limited level of accessibility and are often used for 
# inheritance purposes.

# Information Hiding: Encapsulation facilitates information hiding, which 
# means hiding the internal details and complexities of the object from 
# other objects or code. The object exposes only the necessary information 
# and functionality through its public interface, while keeping the internal 
# implementation hidden.

# Data Encapsulation: Encapsulation allows you to encapsulate the data within 
# an object, providing a level of protection against unauthorized access or 
# modifications. By making the attributes private or using accessors and 
# mutators (getters and setters), you can enforce data integrity and ensure 
# that the data is accessed and modified through controlled methods.

# Benefits of Encapsulation: Encapsulation offers several benefits, including:

# Modularity and Maintainability: Encapsulation promotes modular and organized 
# code by encapsulating related data and behavior into self-contained objects. 
# This makes the code easier to understand, maintain, and update.

# Data Protection and Security: Encapsulation helps protect the integrity of the 
# data by controlling access to it. By hiding the internal details and providing 
# controlled access through methods, you can prevent accidental or unauthorized 
# modifications to the data.

# Code Reusability: Encapsulated objects can be easily reused in different parts 
# of a program or in different programs altogether. The public interface of the 
# object provides a consistent way to interact with it, regardless of its internal 
# implementation.

class Car:
    def __init__(self):
        self.__fuel = 0

    def add_fuel(self, amount):
        self.__fuel += amount

    def drive(self):
        if self.__fuel > 0:
            print("The car is driving.")
            self.__fuel -= 1
        else:
            print("Out of fuel. Please add fuel.")

    def get_fuel_level(self):
        return self.__fuel


my_car = Car()
my_car.add_fuel(50)
my_car.drive()
fuel_level = my_car.get_fuel_level()
print(f"Fuel level: {fuel_level}")
