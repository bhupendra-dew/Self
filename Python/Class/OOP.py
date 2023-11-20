'''
class Dog:
    attr1 = "mammal"
    def __init__(self, name) -> None:
        self.name = name
        pass
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is a {}".format(Tommy.__class__.attr1))

print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
'''
'''
class Dog:
    attr1 = "mammal"
    def __init__(self, name) -> None:
        self.name = name
        pass
    def speak(self):
        print("My name is {}".format(self.name))
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

Rodger.speak()
Tommy.speak()
'''
'''
class Person(object):
    def __init__(self, name, idnumber) -> None:
        self.name = name
        self.idnumber = idnumber
        pass
    def display(self):
        print(self.name)
        print(self.idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))

class Employee(Person):
    def __init__(self, name, idnumber, salary, post) -> None:
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
        return super().details()
    
a = Employee("Rahul", 886012, 200000, "Intern")
a.display()
a.details()
'''
'''
class Student:
    def __init__(self, studentName, studentSurname, studentRollNo) -> None:
        self.name = studentName
        self.surname = studentSurname
        self.rollNo = studentRollNo
        pass

    def getStudentDetails(self):
        print("The name of the student is", self.name, self.surname)
        print("The roll number of the student is", self.rollNo)

student1 = Student("Ashu", "Dewangan", 17)
student1.getStudentDetails()
'''
'''
class MyClass:
    __hiddenVariable = 0
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)
myObject = MyClass()
myObject.add(2)
myObject.add(5)
print(myObject.__hiddenVariable)
'''
'''
class Dog:
    
    attr1 = 'mammal'
    attr2 = 'dog'
    attr3 = 'bark'

    def fun(self):
        print("I am a", self.attr1)
        print("I am a", self.attr2)

    def speak(self):
        print("I can", self.attr3)

Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()
#Rodger.speak()
'''
'''
class Ashu:
    def __init__(self, name, company) -> None:
        self.name = name
        self.company = company
        pass

    def show(self):
        print("Hello my name is", self.name, "and I work in", self.company+".")

object = Ashu("Bhupendra", "Epic Games")
object.show()
'''
'''
class Ashu:
    def __init__(BD, name, company) -> None:
        BD.name = name
        BD.company = company
        pass

    def show(BD):
        print("Hello my name is", BD.name, "and I work in", BD.company + ".")

obj = Ashu("Bhupendra", "Ubisoft")
obj.show()
'''

# Self
'''
class mynumber:
    def __init__(self, value) -> None:
        self.value = value
        pass

    def print_value(self):
        print(self.value)

object1 = mynumber(int(input("Enter the number:")))
object1.print_value()
'''
'''
class Subject:
    def __init__(self, attr1, attr2) -> None:
        self.attr1 = attr1
        self.attr2 = attr2
        pass

object = Subject('Maths', 'Science')
print(object.attr1)
print(object.attr2)
'''

'''
class Cars():
    def __init__(self, company, model, color) -> None:
        self.company = company
        self.model = model
        self.color = color
        pass

    def show(self):
        print("The Company is :", self.company)
        print("The model is :", self.model)
        print("The Color is :", self.color)

audi = Cars("Audi", "A4", "Blue")
ferrari = Cars("Ferrari", "Ferrari 488", "red")
lemborgani = Cars("Lemborgani", "Hurrican", "Black")
dodge = Cars("Dodge", "Hell Cat", "Purple")

audi.show()
ferrari.show()
lemborgani.show()
dodge.show()

print("The company of the car is", audi.company)
print("The color of the car is", audi.color)
print("The model of the dodge is", dodge.model)
print("The model of Lemborgani is", lemborgani.model)
'''

'''
class Dog:
    animal = 'dog'
    def __init__(self, breed, color) -> None:
        self.breed = breed
        self.color = color
        pass

Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print("Rodger details:")
print("Rodger is a", Rodger.animal)
print("Breed:", Rodger.breed)
print("Color:", Rodger.color)

print("\nBuzo details:")
print("Buzo is a", Buzo.animal)
print("Breed:", Buzo.breed)
print("Color:", Buzo.color)

print("\nAccessing class variable using class name.")
print(Dog.animal)
'''

'''
class Dog:
    animal = "dog"
    def __init__(self, breed) -> None:
        self.breed = breed
        pass
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())
'''

# Creating a simple class in Python
'''
class Animal:
    def __init__(self, name) -> None:
        self.name = name
        pass
    def speak(self):
        return f"{self.name} says Hello!!!"
    
dog = Animal("Ishaan")
cat = Animal("Pussy")
print(dog.speak())
print(cat.speak())
'''

# Creating a subclass(Inheritance)
'''
class Anime:
    def __init__(self, name) -> None:
        self.name = name
        pass

    def Name(self):
        return f"The anime name is {self.name}"
    
class OP(Anime):
    def Name(self):
        return f"The main character is {self.name}"
    
anime = Anime("One Punch MAN")
op = OP("Sitama")

print(anime.Name())
print(op.Name())
'''

# Using the super() function
'''
class Animal:
    def __init__(self, name) -> None:
        self.name = name
        pass
    def speak(self):
        return f"{self.name} says hello!"
    
class Dog(Animal):
    def __init__(self, name, breed) -> None:
        super().__init__(name)
        self.breed = breed

dog = Dog("Charlie", "Bulldog")
print(dog.name)
print(dog.breed)
'''

# Creating a property
'''
class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius
        pass
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

circle = Circle(5)
print(circle.radius)
circle.radius = 10
print(circle.radius)
'''

# Encapsulation - Private members
'''
class MyClass:
    def __init__(self) -> None:
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"
        pass

obj = MyClass()
print(obj.public)
print(obj._protected)
#print(obj.__private)
'''

# Polymorphism - Using Inbuilt Abstract Base Classes(ABC)
'''
from collections.abc import Iterable

def get_length(item):
    if isinstance(item, Iterable):
        return len(item)
    else:
        return "Not iterable"
    
print(get_length("Hello"))
print(get_length([1, 2, 3]))
print(get_length(123))
'''

# Defining an Abstract Base Class(ABC)
'''
from abc import ABC, abstractmethod
class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(AbstractAnimal):
    def speak(self):
        return "Boww Boww!!!"
    
dog = Dog()
print(dog.speak())
'''

# Using class methods and static methods
'''
class MyClass:
    @classmethod
    def class_method(cls):
        return "Class method called"
    @staticmethod
    def static_method():
        return "Static method called"
    
print(MyClass.class_method())
print(MyClass.static_method())
'''

# Operator Overloading in Python
'''
class Mango:
    def __init__(self, x) -> None:
        self.x = str(x)
        pass

    def __add__(self, y):
        return self.x + y.x
    
obj1 = Mango(140)
obj2 = Mango('mangoes')
print(obj1 + obj2)
'''

# Using Special methods for string representations(repr and str)
'''
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        pass

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."
    
    def __repr__(self) -> str:
        return f"Person('{self.name}', '{self.age})"
    
p = Person("Bob", 30)
print(str(p))
print(repr(p))
'''

# Using composite in Pyhton OOP
'''
class Salary:
    def __init__(self, pay, bonus) -> None:
        self.pay = pay
        self.bonus = bonus
        pass

class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        pass

s = Salary(15000, 5000)
e = Employee("Ashwin", s)
print(e.salary.pay)
print(e.salary.bonus)
'''

# Using multiple inheritance
'''
class Parent1:
    def method1(self):
        return "Parent1's method called"

class Parent2:
    def method2(self):
        return "Parent2's method called"
    
class Child(Parent1, Parent2):
    pass

c = Child()
print(c.method1())
print(c.method2())
'''

# Implementing Decorators within classes
'''
class MyClass:
    @staticmethod
    def method():
        return "Static method called"
    
    @classmethod
    def classmethod(cls):
        return "Class method called"
    
print(MyClass.method())
print(MyClass.classmethod())
'''

# Creating a Singleton class in Python
'''
class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance
    
    def __init__(self) -> None:
        if Singleton._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self
        pass

s = Singleton.getInstance()
print(s)
'''

# Using Mixin classes in Python

class Mixin1(object):
    def test(self):
        print("Mixin1")

class Mixin2(object):
    def test(self):
        print("Mixin2")

class MyClass(Mixin1, Mixin2):
    pass

obj = MyClass()
obj.test()
