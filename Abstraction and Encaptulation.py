#!/usr/bin/env python
# coding: utf-8

# Q1. What is Abstraction in OOps? Explain with an example.
# 
# Ans. In object-oriented programming (OOP), abstraction refers to the concept of hiding complex implementation details and exposing only the essential features or behaviors of an object or a class. It allows us to focus on what an object does rather than how it does it.
# 
# Abstraction is achieved through the use of abstract classes and interfaces. An abstract class is a class that cannot be instantiated and serves as a blueprint for other classes. It may contain abstract methods, which are declared but not implemented in the abstract class. Concrete classes that inherit from the abstract class must provide implementations for these abstract methods.
# 
# Let's take an example of a shape hierarchy to understand abstraction. Consider that we want to create different shapes like a circle, square, and rectangle. Each shape has a different calculation for its area and perimeter. We can define an abstract class called "Shape" that contains abstract methods for calculating area and perimeter:

# In[8]:


# Python program demonstrate  
# abstract base class work   
from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
          
# Driver code   
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  


# In[ ]:


Q2. Differentiate between Abstraction and Encapsulation. Explain with an example


# Ans. Abstraction and encapsulation are both fundamental concepts in object-oriented programming, but they serve different purposes. Let's understand the differences between them and explain each concept with an example:
# 
# Abstraction:
# 
# Abstraction focuses on hiding unnecessary details and exposing only the essential features or behaviors of an object or a class.
# It allows us to work with high-level concepts rather than dealing with low-level implementation details.
# Abstraction is achieved through the use of abstract classes and interfaces in OOP.
# Example:
# Consider a car as an object. When we think about a car, we are concerned with its essential features such as starting the engine, accelerating, braking, and turning. We don't need to know how these features are implemented internally. This is an example of abstraction. We abstract away the complex mechanics and focus on the car's functionalities from a higher level.
# 
# In code, we can define an abstract class called "Car" that declares abstract methods for these essential features:

# In[14]:


import abc
abstract class Car {
    abstract void startEngine();
    abstract void accelerate();
    abstract void brake();
    abstract void turn();
}


# In[15]:


from abc import ABC, abstractmethod


class BankAccount {
    private int accountNumber;
    private double balance;
    private String customerName;
    
    public void deposit(double amount) {
        // Implementation to deposit the specified amount
    }
    
    public void withdraw(double amount) {
        // Implementation to withdraw the specified amount
    }
    
    public double getBalance() {
        // Implementation to return the account balance
    }
}


# Q.4 How can we achieve data abstraction?
# 
# 
# In object-oriented programming, data abstraction can be achieved through the use of classes, where the internal data representation and implementation details are hidden from the outside world. Here are the key steps to achieve data abstraction:
# 
# Define a class: Start by defining a class that represents the abstraction you want to create. The class should encapsulate the necessary data and provide methods for accessing and manipulating that data.
# 
# Access modifiers: Use access modifiers such as private, protected, and public to control the visibility and accessibility of class members (variables and methods). By making data members private, you hide them from direct access outside the class.
# 
# Getter and setter methods: Provide getter and setter methods (also known as accessor and mutator methods) to access and modify the private data members. These methods act as intermediaries and allow controlled access to the data.
# 
# Data validation: Implement data validation logic within the setter methods to enforce any constraints or rules on the data. This ensures that the data remains consistent and valid throughout the object's lifecycle.

# Q.5 Can we create an instance of an abstract class? Explain your answer
# 
# Ans. No, we cannot create an instance of an abstract class in most programming languages, including Python.
# 
# An abstract class is a class that is meant to be subclassed and serves as a blueprint for creating derived classes. It contains one or more abstract methods that are declared but not implemented in the abstract class. These abstract methods act as placeholders, defining a contract that any concrete subclass must fulfill by providing implementations for those methods.
# 
# The purpose of an abstract class is to define a common interface and structure for related classes. It cannot be instantiated on its own because it may have incomplete or undefined behavior due to the lack of implementations for the abstract methods. Therefore, attempting to create an instance of an abstract class would not make sense and typically leads to an error.
# 
# In Python, if you try to create an instance of an abstract class that contains abstract methods using the abc module, it will raise a TypeError with a message stating that the abstract class cannot be instantiated. This behavior is enforced by the ABC metaclass used by the abc module.
# 
# To use the functionality provided by an abstract class, you need to create concrete subclasses that inherit from the abstract class and provide implementations for all the abstract methods. Instances of these concrete subclasses can be created and used according to the defined interface and behavior.
