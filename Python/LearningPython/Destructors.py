# Python program to illustrate destructor 
'''
class Employee:
    # Initializing 
    def __init__(self) -> None:
        print("Employee created")
        pass
    # Deleting (Calling destructor)
    def __del__(self):
        print("Destructor Called, Employee deleated")
obj = Employee()
del obj
'''

# Python program to illustratw destructor 
'''
class Employee:
    # Initializing
    def __init__(self) -> None:
        print("Employee Created.")
        pass
    # Calling Destructor
    def __del__(self):
        print("Destructor called")
def Create_obj():
    print('Making Object....')
    obj = Employee()
    print("function end....")
    return obj

print("Calling Create_obj() function....")
obj = Create_obj()
print("Program End....")
'''

# Python program to illustrate destructor
'''
class A:
    def __init__(self, bb) -> None:
        self.b = bb
        pass
class B:
    def __init__(self) -> None:
        self.a = A(self)
        pass
    def __del__(self):
        print("die")
def fun():
    b = B()
fun()
'''

# Destruction in recursion

class RecursiveFunction:
    def __init__(self, n) -> None:
        self.n = n
        print("Recursive function initialized with n =", n)
        pass
    def run(self, n = None):
        if n is None:
            n = self.n
        if n <= 0:
            return
        print("Running recursive function with n =", n)
        self.run(n - 1)
    def __del__(self):
        print("Recursive function object destroyed..")
# Create an object of the class 
obj = RecursiveFunction(10)
# Calling the recursive function
obj.run()
# Destroy the object
del obj
