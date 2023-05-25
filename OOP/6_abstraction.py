# Abstraction is a fundamental concept in object-oriented programming (OOP) 
# that focuses on representing essential features and behavior while hiding 
# unnecessary details. It allows you to create simplified models of real-world 
# entities or systems, emphasizing what is important and suppressing the 
# irrelevant or complex aspects.

# Here are the key aspects of abstraction:

# Simplification: Abstraction simplifies the representation of complex 
# systems or entities by focusing on the essential features and behavior. 
# It captures the core attributes, methods, and relationships that are 
# relevant to the problem domain, while omitting the intricate details.

# Data Abstraction: Data abstraction involves representing data by abstracting 
# away the internal implementation details and exposing only the necessary 
# information. It defines the properties (attributes) of an object without 
# specifying how they are implemented. Data abstraction provides a way to 
# define the structure and behavior of data types without revealing the 
# underlying complexity.

# Procedure Abstraction: Procedure abstraction focuses on hiding the 
# implementation details of methods or functions. It defines the 
# interface (method signature) and functionality of a method without 
# exposing the internal workings. Procedure abstraction allows users 
# to interact with the methods without needing to know the underlying 
# implementation.

# Encapsulation and Abstraction: Abstraction is closely related to 
# encapsulation. Encapsulation combines data and methods into a single 
# unit (object) and provides controlled access to them. Abstraction, on 
# the other hand, focuses on presenting a simplified view of the object's 
# essential features and behavior while hiding the internal details. 
# Encapsulation supports abstraction by providing a way to encapsulate 
# the implementation details within an object.

# Class and Interface: Abstraction is often achieved through the use of 
# classes and interfaces in OOP. A class represents a blueprint for creating 
# objects and defines the structure, behavior, and relationships of objects. 
# An interface defines a contract or set of method signatures that a class must 
# implement. Both classes and interfaces can serve as abstractions by providing 
# a simplified view and hiding the implementation details.

# Benefits of Abstraction: Abstraction offers several benefits, including:

# Simplification and Focus: Abstraction simplifies complex systems by focusing 
# on the essential aspects, making the code easier to understand, manage, and maintain.

# Modularity and Flexibility: Abstraction promotes modularity by breaking down 
# complex systems into smaller, self-contained units. This allows for easier 
# development, testing, and modification of the system's components without 
# impacting the entire system.

# Code Reusability: Abstraction facilitates code reuse by providing abstract 
# classes or interfaces that can be implemented by multiple classes. This promotes 
# code modularity and reduces redundancy.

# Security and Privacy: Abstraction allows you to hide sensitive or private 
# information and expose only what is necessary. It helps in protecting the 
# integrity of data and preventing unauthorized access.

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Creating objects of different subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Polymorphic behavior through abstraction
animals = [dog, cat]

for animal in animals:
    animal.make_sound()
    animal.eat()
