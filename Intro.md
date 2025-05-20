# 🧠 Object-Oriented Programming (OOP) Summary

## 🔹 Class  
A **blueprint** for creating objects. It defines the **structure** (attributes) and **behavior** (methods) of objects.  
**Example:** A `Car` class can define how all cars should look and behave.  

```python
class Car:
    pass
```

## 🔹 Object  
An **instance** of a class. It holds real data and can use the class methods.  
**Example:** A `my_car` object of class `Car` with color red and model 2022.  

```python
my_car = Car()
```

## 🔹 Attributes  
**Variables** inside the class that store object data. Usually defined in the constructor.  
**Example:** A car has `color`, `brand`, and `year`.

```python
class Car:
    def __init__(self, color, brand, year):
        self.color = color
        self.brand = brand
        self.year = year
```

## 🔹 Constructor (`__init__`)  
A **special method** that runs automatically when we create an object. It sets up initial values.  

```python
my_car = Car("Red", "Toyota", 2022)
```

## 🔹 Instance Method  
A **function** defined in a class that works with a specific object. It uses `self` to access data.

```python
class Car:
    def start_engine(self):
        print("Engine started!")
```

## 🔹 Static Method  
A method that **does not use** object or class data. It's like a helper inside the class.  
Use `@staticmethod` decorator.

```python
class MathTools:
    @staticmethod
    def add(a, b):
        return a + b
```

## 🔹 Class Method  
A method that works with the **class itself**, not an object. Use `cls` instead of `self`.  
Use `@classmethod` decorator.

```python
class Car:
    wheels = 4

    @classmethod
    def car_info(cls):
        print(f"All cars have {cls.wheels} wheels.")
```

## 🔹 Class Attributes (Static Attributes)  
Variables shared by **all objects** of the class. Defined outside `__init__`.

```python
class Car:
    wheels = 4  # All cars have 4 wheels
```

## 🔹 Inheritance  
A class can **inherit** from another class to reuse its code.  
**Example:** `ElectricCar` can inherit from `Car`.

```python
class ElectricCar(Car):
    def charge(self):
        print("Charging battery...")
```

## 🔹 Polymorphism  
Many classes can have methods with the **same name** but different behaviors.

```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def animal_sound(animal):
    animal.speak()  # Same method name, different results
```

## 🔹 Encapsulation  
Hiding internal details by using **private attributes** and providing **get/set methods**.  
It protects data from being accessed directly.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
```


This Python File applying what above
[View my Python script](https://github.com/MohammedNoureldeen/DeepDive1/blob/main/OOP/OOP.py)
