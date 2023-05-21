# Inheritance is a fundamental concept in object-oriented 
# programming (OOP) that allows classes to inherit attributes 
# and methods from other classes. It is a mechanism that promotes 
# code reuse and facilitates the creation of hierarchical 
# relationships between classes.

# Inheritance involves two types of classes: a base class (also 
# called a superclass or parent class) and a derived class (also 
# called a subclass or child class). The derived class inherits 
# the attributes and methods of the base class, extending or 
# modifying them as needed.

# Here are the key points about inheritance:

# Base Class: The base class is the class that is being inherited 
# from. It defines the common attributes and methods shared by 
# multiple related classes.

# Derived Class: The derived class is the class that inherits 
# from the base class. It extends or specializes the base class 
# by adding new attributes or methods, or by overriding existing ones.

# Inheritance Syntax: To define a derived class, you specify the 
# base class name in parentheses after the derived class name in 
# the class definition.

# Attributes and Methods Inheritance: The derived class inherits 
# all the attributes and methods of the base class. It can access 
# and use them as if they were defined in the derived class itself.

# Overriding: The derived class can override (redefine) the methods 
# of the base class to provide its own implementation. This allows 
# customization and specialization of behavior.

# Access Modifiers: In some programming languages, inheritance can be 
# affected by access modifiers such as public, protected, or private, 
# which control the visibility and accessibility of inherited members.

# Multiple Inheritance: Some languages support multiple inheritance, 
# where a derived class can inherit from multiple base classes. This allows 
# a class to inherit attributes and methods from multiple sources.

# Inheritance promotes code reuse, modularity, and extensibility. It allows 
# you to create a hierarchy of classes, with more specialized subclasses 
# inheriting from more general base classes. This approach facilitates the 
# organization and maintenance of code by grouping related functionality 
# together and reducing duplication.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def speak(self):
        print("The dog barks.")


class Cat(Animal):
    def speak(self):
        print("The cat meows.")


animal = Animal("Generic Animal")
animal.speak()   # Output: The animal makes a sound.

dog = Dog("Rex")
dog.speak()      # Output: The dog barks.

cat = Cat("Whiskers")
cat.speak()      # Output: The cat meows.
