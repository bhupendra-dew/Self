# Python program to demonstarate inheritance
'''

class Person(object):
    # Constructor 
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        pass
    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)
# Driver Code
emp = Person("Satyam", 103) # Ant of Person
emp.Display()

'''
# #### ERROR #######
# # Creating a child class
'''
class Emp(person):
    def Print(self):
        print("Emp class called")
Emp_details = Emp("Ashu", 1)
# calling parent class function
Emp_details.Display()
# calling child class function
Emp_details.Print()
'''
'''
class Person(object):
    # Constructor 
    def __init__(self, name) -> None:
        self.name = name
        pass
    # To get name 
    def getName(self):
        return self.name
    # To check if this person is an employee
    def isEmployee(self):
        return False
# INherited or Subclass
class Employee(Person):
    def isEmployee(self):
        return True
    
# Driver code
emp = Person("Geek1")
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2")
print(emp.getName(), emp.isEmployee())
'''

# Python code to demnostrate how parent constructors are called.
# Parent class
'''
class Person(object):
    # __init__ is known as the constructor 
    def __init__(self, name, idnumber) -> None:
        self.name = name
        self.idnumber = idnumber
        pass
    def display(self):
        print(self.name)
        print(self.idnumber)
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post) -> None:
        self.salary = salary
        self.post = post
        super().__init__(name, idnumber, salary, post)
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee("Rahul", 488465, 8484545, "Intern")
# Calling a function of the class person using its instance
a.display()
'''
## ERROR ###
'''
class A:
    def __init__(self, n = "Rahul") -> None:
        self.name = n
        pass
class B(A):
    def __init__(self, roll) -> None:
        self.roll = roll
object = B(23)
print(object.name)
'''
'''
# parent class
class Person():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        pass
    def display(self):
        print(self.name, self.age)
    # child class
    class Student(Person):
        def __init__(self, name, age):
            self.sName = name
            self.sAge = age
            # inheriting the properties of parent class
            super().__init__("Rahul", age)
        def displayINfo(self):
            print(self.sName, self.sAge)
obj = Student("Mayak", 23)
obj.display()
obj.displayInfo()
'''

"""
# parent class
class Person():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        pass

    def display(self):
        print(self.name, self.age)

# child class
class Student(Person):
    def __init__(self, name, age, dob) -> None:
        self.sName = name
        self.sAge = age
        self.dob = dob
        # inheriting the properties of parent class
        super().__init__("Rahul", age)

    def displayInfo(self):
        print(self.sName, self.sAge, self.dob)

obj = Student("Mayank", 23, "16 - 03 - 2000")
obj.display()
obj.displayInfo()
"""


# Python example to show the working of multiple inheritance
'''
class Base1(object):
    def __init__(self) -> None:
        self.str1 = "Geek1"
        print("Base1")
        pass

class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")
        pass

class Derived(Base1, Base2):
    def __init__(self) -> None:
        # calling constructors of Base1 and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)

ob = Derived()
ob.printStrs()
'''


# Python program to demonstrate inheritane, base or Super class. Note 
# { Generally, object is made ancestor of all classes, IN Pyhton 3.x "class person" is equivalent to "class Person(object)" } 
'''

class Base(object):
    # constuctor 
    def __init__(self, name) -> None:
        self.name = name
        pass
    # To get name 
    def getName(self):
        return self.name
    
# Inherited or sub class (Note Person in bracket)
class Child(Base):
    # Constructor
    def __init__(self, name, age) -> None:
        Base.__init__(self, name)
        self.age = age
        
    # To get age
    def getAge(self):
        return self.age
    
# Inherited or Sub class (Note Person in bracket)

class GrandChild(Child):
    # Constructor
    def __init__(self, name, age, address) -> None:
        Child.__init__(self, name, age)
        self.address = address
        super().__init__(name, age, address)
    # TO get Address
    def getAddress(self):
        return self.address 
    
# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())
'''


# Python program to demonstrate single inheritance
'''
# Base class

class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class

class Child(Parent):
    def func2(self):
        print("This function is in child class.")

# Driver's code
object = Child()
object.func1()
object.func2()
'''

# Python program to demonstrate multiple inheritance
'''
# Base class1
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

# Base class2
class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

# Drivers code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1. parents()
'''

# Python program to demonstrate multilevel inheritance
'''
# Base class

class Grandfather:
    def __init__(self, grandfathername) -> None:
        self.grandfathername = grandfathername
        pass
# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername) -> None:
        self.fathername = fathername
        # Invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)
        super().__init__(fathername, grandfathername)

# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername) -> None:
        self.sonname = sonname
        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)
        
    def print_name(self):
        print("Grandfather name :", self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)

# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()

'''

# Pyhton program to demonstrate Hierarchical inheritance

class Parent:
    def func1(self):
        print("Ye function ek parent class hai.")

class child1(Parent):
    def func2(self):
        print("Ye function child 1")
        
class child2(Parent):
    def func3(self):
        print("Ye child 2 hai")
    
object1 = child1()
object2 = child2()
object1.func1()
object1.func2()
object1.func1()
object1.func3()
