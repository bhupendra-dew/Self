'''
class Item:
    pay_rate = 0.8   # The pay rate after 20 % discount
    def __init__(self, name : str, price : float, quantity = 0) -> None:

        # Run valaditions to recive arguements 
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        # Assing to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute 
        Item.all.append(self)

        pass

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

for instance in Item.all:
    print(instance.name)
'''
'''
class Item:
    pay_rate = 0.8 # The payrate after 20 % discount
    def __init__(self, name : str, price : float, quantity = 0) -> None:
        print(f"An instance created for : {name}")
        
        # Run validations to the recived arguments

        assert price >= 0, f"Price {price} is not greater that or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
        
        # Assign to self ohbject
        self.name = name
        self.price = price
        self.quantity = quantity
        pass
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item("Phone", 100, 10)
item2 = Item("Laptop", 1000, 50)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

print(Item.__dict__)        # All the attributes for Class level
print(item1.__dict__)       # All the attributes for instance level

item1.apply_discount()
print(item1.price)
'''
'''
class Dog:
    # Class attribute 
    attr1 = "mammal"
    # Instance attribute
    def __init__(self, name) -> None:
        self.name = name
        pass

# Driver code
# Obejective attribute
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
# Acessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
'''
'''
class Dog:
    # class attribute
    attr1 = "mammal"
    # Instance attribute
    def __init__(self, name) -> None:
        self.name = name
        pass
    def speak(self):
        print("My name is {}".format(self.name))

# Driver code objective instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
# Acessing class metods
Rodger.speak()
Tommy.speak()
'''

"""

# Python cod e to demonstrate how parent constructors are called
# parent class
class Person(object):
    # __init__ is known as the constructor
    def __init__(self, name, idnumber) -> None:
        self.name = name
        self.idnumber = idnumber
        pass
    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}". format(self.name))
        print('IdNumber : {}'.format(self.idnumber))
        
# child Class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post) -> None:
        self.salary = salary
        self.post = post
        super().__init__(name, idnumber)

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber : {}".format(self.idnumber))
        print("Post : {}".format(self.post))
        return super().details()
    
# Creation of an object variable or an instance
a = Employee("Rahul", 664113, 1548453, "Intern")

# Calling a function of the class Person using its instance
a.display()
a.details()
"""

# Python Polymorphism


"""
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
        return super().flight()
    
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
"""

"""

# Python program to demonstrate private members
# Creating a Base class
class Base:
    def __init__(self) -> None:
        self.a = "GeeksforGeeks"
        self.__c = "GeeksForGeeks"
        pass
# Creating a derived class
class Derived(Base):
    def __init__(self) -> None:
        # Calling constructor of base class
        Base.__init__(self)
        print("Calling private member of base class : ")
        print(self.__c)
        super().__init__()

# Driver code
obj1 = Base()
print(obj1.a)
# Uncommenting print(obj1.c) will raise an AttributeError
# Uncommenting obj2 = Derived() will also raise an AttributeError as private member of base class is called inside derived class

"""
"""
class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 0
    # A member method that changes __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print(self.__hiddenVariable)
# Driver Code
myObject = MyClass()
myObject.add(2)
myObject.add(5)
# This line causes error
print(myObject.__hiddenVariable)
"""
'''
# A python program to demonstrate that hidden members can be accessed outside a class
class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 10
# Driver code
myObject = MyClass()
print(myObject._MyClass__hiddenVariable)
'''
'''
class Test:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        pass
    def __repr__(self) -> str:
        return "Test a:%s b:%s" % (self.a, self.b)
        pass
    def __str__(self) -> str:
        return "From str method of Test : a is %s,"" b is %s" % (self.a, self.b)
        pass

# Driver Code 
t = Test(1234, 5678)
print(t)        # Test calls __str__()
print(([t]))    # Test calls __repr__()
'''
"""
class Test:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        pass
    def __repr__(self) -> str:
        return "Test a:%s b:%s" % (self.a, self.b)
        pass
# Driver code
t = Test(1234, 5678)
print(t)
"""
'''
class Test:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        pass

# Driver Code
t = Test(1234, 5678)
print(t)
'''



##### OBject orientated Programming in Python ######

class Student:
    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade ### 0 to 100
        pass

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students) -> None:
        self.name = name
        self.max_students = max_students
        self.max_students = []
        pass

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        pass
    