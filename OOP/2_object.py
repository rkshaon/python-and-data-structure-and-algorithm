# In object-oriented programming (OOP), an object is 
# an instance of a class. It is a fundamental concept 
# that represents a specific entity or data structure 
# with its own set of attributes (data) and behaviors (methods). 
# Objects are created based on a class definition, which 
# serves as a blueprint or template for creating multiple 
# instances of the same type.

# Here are some key points about objects:

# Instance: An object is an instance of a class. 
# When you create an object, you are creating a 
# unique instance of that class, with its own set 
# of attribute values.

# Attributes: Objects have attributes, also known 
# as properties or instance variables, which store 
# the object's data. These attributes can be of 
# different data types, such as integers, strings, 
# lists, or even other objects.

# Methods: Objects have methods, which are functions 
# associated with the object's behavior. Methods 
# define the actions that an object can perform 
# and can interact with the object's attributes.

# Identity: Each object has a unique identity that 
# distinguishes it from other objects. The identity 
# is usually assigned automatically by the programming 
# language and can be used to compare or identify objects.

# Encapsulation: Objects encapsulate their data and 
# methods, meaning they bundle related data and behavior 
# together into a single entity. This helps in organizing 
# and managing complex systems and promotes code reusability.

# Abstraction: Objects provide abstraction by hiding the 
# internal details of their implementation and exposing 
# only the necessary interfaces. This allows users of the 
# object to interact with it without needing to know the 
# underlying implementation.

# Interactions: Objects can interact with each other by 
# invoking methods or accessing attributes of other objects. 
# These interactions enable collaboration and communication 
# between different objects in an object-oriented system.

# By creating and manipulating objects, you can model real-world 
# entities or abstract concepts in your code, representing them 
# as self-contained units with their own state and behavior. 
# Objects facilitate the organization, modularity, and reusability 
# of code in object-oriented programming.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.make} {self.model}'s engine is now running.")
        else:
            print(f"The {self.make} {self.model}'s engine is already running.")

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.make} {self.model}'s engine has been stopped.")
        else:
            print(f"The {self.make} {self.model}'s engine is already stopped.")

    def drive(self):
        if self.is_running:
            print(f"The {self.make} {self.model} is now driving.")
        else:
            print(f"Cannot drive the {self.make} {self.model} because the engine is not running.")


# Creating car objects
car1 = Car("Honda", "Civic", 2021)
car2 = Car("Toyota", "Corolla", 2022)

# Accessing attributes
print(car1.make)   # Output: Honda
print(car2.year)   # Output: 2022

# Calling methods
car1.start_engine()   # Output: The Honda Civic's engine is now running.
car2.drive()          # Output: Cannot drive the Toyota Corolla because the engine is not running.

car1.drive()          # Output: The Honda Civic is now driving.

car2.start_engine()   # Output: The Toyota Corolla's engine is now running.
car2.stop_engine()    # Output: The Toyota Corolla's engine has been stopped.
