# OOP in Python
Object oriented programming (OOP) in Python is a programming paradigm that uses objects and classes to model real-world entities and their relations. Some main features of OOP in Python are:
- Classes
- Objects
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction
- Modularity

# Class
In Python, a class is a blueprint for creating objects (instances) that share similar attributes and behavior. It provides a way to define and organize code in a structured manner, allowing you to create reusable and modular code.

Class [Example](https://github.com/rkshaon/python-and-data-structure-and-algorithm/blob/master/OOP/1_class.py).

# Object
In object-oriented programming (OOP), an object is an instance of a class. It is a fundamental concept that represents a specific entity or data structure with its own set of attributes (data) and behaviors (methods). Objects are created based on a class definition, which serves as a blueprint or template for creating multiple instances of the same type.

Here are some key points about objects:
- Instance: An object is an instance of a class. When you create an object, you are creating a unique instance of that class, with its own set of attribute values.
- Attributes: Objects have attributes, also known as properties or instance variables, which store the object's data. These attributes can be of different data types, such as integers, strings, lists, or even other objects.
- Methods: Objects have methods, which are functions associated with the object's behavior. Methods define the actions that an object can perform and can interact with the object's attributes.
- Identity: Each object has a unique identity that distinguishes it from other objects. The identity is usually assigned automatically by the programming language and can be used to compare or identify objects.
- Encapsulation: Objects encapsulate their data and methods, meaning they bundle related data and behavior together into a single entity. This helps in organizing and managing complex systems and promotes code reusability.
- Abstraction: Objects provide abstraction by hiding the internal details of their implementation and exposing only the necessary interfaces. This allows users of the object to interact with it without needing to know the underlying implementation.
- Interactions: Objects can interact with each other by invoking methods or accessing attributes of other objects. These interactions enable collaboration and communication between different objects in an object-oriented system.

By creating and manipulating objects, you can model real-world entities or abstract concepts in your code, representing them as self-contained units with their own state and behavior. Objects facilitate the organization, modularity, and reusability of code in object-oriented programming.

Object [Example](https://github.com/rkshaon/python-and-data-structure-and-algorithm/blob/master/OOP/2_object.py).

# Inheritance
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows classes to inherit attributes and methods from other classes. It is a mechanism that promotes code reuse and facilitates the creation of hierarchical relationships between classes.

Inheritance involves two types of classes: a base class (also called a superclass or parent class) and a derived class (also called a subclass or child class). The derived class inherits the attributes and methods of the base class, extending or modifying them as needed.

Here are the key points about inheritance:
- Base Class: The base class is the class that is being inherited from. It defines the common attributes and methods shared by multiple related classes.
- Derived Class: The derived class is the class that inherits from the base class. It extends or specializes the base class by adding new attributes or methods, or by overriding existing ones.
- Inheritance Syntax: To define a derived class, you specify the base class name in parentheses after the derived class name in the class definition.
- Attributes and Methods Inheritance: The derived class inherits all the attributes and methods of the base class. It can access and use them as if they were defined in the derived class itself.
- Overriding: The derived class can override (redefine) the methods of the base class to provide its own implementation. This allows customization and specialization of behavior.
- Access Modifiers: In some programming languages, inheritance can be affected by access modifiers such as public, protected, or private, which control the visibility and accessibility of inherited members.
- Multiple Inheritance: Some languages support multiple inheritance, where a derived class can inherit from multiple base classes. This allows a class to inherit attributes and methods from multiple sources.

Inheritance promotes code reuse, modularity, and extensibility. It allows you to create a hierarchy of classes, with more specialized subclasses inheriting from more general base classes. This approach facilitates the organization and maintenance of code by grouping related functionality together and reducing duplication.

Inheritance [Example](https://github.com/rkshaon/python-and-data-structure-and-algorithm/blob/master/OOP/3_inheritance.py).

# Polymorphism
Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables the same code to be used with different types of objects, providing flexibility and extensibility in software design.

Polymorphism involves the following key ideas:
- Inheritance: Polymorphism relies on inheritance to create a hierarchical relationship between classes. By defining a common superclass and deriving multiple subclasses from it, polymorphism allows objects of these subclasses to be treated as instances of the superclass.
- Method Overriding: Polymorphism is often achieved through method overriding. Subclasses can override methods inherited from the superclass, providing their own implementation while keeping the method signature (name and parameters) the same. This allows different subclasses to have specialized behavior for the same method.
- Method Invocation: Polymorphism enables objects of different classes to be invoked using the same method name. The actual behavior of the method is determined dynamically at runtime based on the actual type of the object being referenced.
- Interface Compatibility: Polymorphism requires that the objects involved exhibit interface compatibility. This means that they share a common set of methods or behaviors defined in a common superclass or interface. The code that interacts with these objects can use the methods defined in the common interface, regardless of the specific type of object.

The key benefit of polymorphism is that it allows for code reuse, extensibility, and flexibility. It promotes modular and flexible designs by allowing different classes to conform to a common interface and be used interchangeably where the common interface is expected.

Polymorphism [Example](https://github.com/rkshaon/python-and-data-structure-and-algorithm/blob/master/OOP/4_polymorphism.py).



# Encapsulation

# Abstraction

# Modularity
