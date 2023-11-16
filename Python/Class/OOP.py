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
