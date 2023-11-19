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

