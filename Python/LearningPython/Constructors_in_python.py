# Printing Geeks For Geeks

'''
class GeeksforGeeks:
    # default constructor
    def __init__(self) -> None:
        self.geek = "Geeks For Geeks"
        pass
    # A method for printing data members
    def print_Geek(self):
        print(self.geek)

# Creating object of the class
obj = GeeksforGeeks()

# Calling the instance method using the object obj
obj.print_Geek()
'''

# Addition of two number
'''
class Additon:
    first = 0 
    second = 0 
    third = 0
    # parameterized constructor
    def __init__(self, f, s) -> None:
        self.first = f
        self.second = s
        pass
    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two number = " + str(self.answer))
    def calculate(self):
        self.answer = self.first + self.second

# Creating object of the class, this will invoke parameterizzed constructor
obj1 = Additon(1000, 2000)
# Creating second object of same class
obj2 = Additon(10, 20)
# Perform Addition on obj1
obj1.calculate()
# Perform Addition on obj2
obj2.calculate()
# display result of obj1
obj1.display()
# display result of obj2
obj2.display()
'''

class MyClass:
    def __init__(self, name = None) -> None:
        if name is None:
            print("Default constructor called")
        else:
            self.name = name
            print("Parameterized constructor called with name", self.name)
        pass
    def method(self):
        if hasattr(self, "name"):
            print("Method called with name", self.name)
        else:
            print("Method called without a name")
# Creating an object of class using the default constructor 
obj1 = MyClass()
# Call a method of the class
obj1.method()
# Create an object of the class using the parameterized constructor
obj2 = MyClass("John")
# Call a method of the class
obj2.method()
