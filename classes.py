 # simple example of class in python
from abc import ABC,abstractmethod
class kartik:
    def __init__(self,name):
        self.name=name
        
    def students(self):
        print(f"{self.name}")
        
obj=kartik("kartik")
obj.students()

# another example of class having magic method which are called constructor of classes

class gautam:
    def __init__(self,param) :
        self.name=param
        
    def __str__(self):
        return self.name
    
obj=gautam("jay")
print(obj)


# class multiple inheritance in python 

class roll:
    def __init__(self):
        print("roll class")
        
class name:
    def __init__(self):
        
        print("name class")
        
class students(roll,name):
    def __init__(self):
        print("students class")
    
obj=students()

# thi is multi-level inheritance
class roll:
    def __init__(self):
        print("roll class")
        
class name(roll):
    def __init__(self):
        
        print("name class")
        
class students(name):
    def __init__(self):
        print("students class")
        
obj=students()

# now we will do method overriding and super method 
class roll:
    def __init__(self):
        print("roll class")
        
class name(roll):
    def __init__(self):
        super().__init__()
        print("name class")
        
class students(name):
    def __init__(self):
        super().__init__()
        
        print("students class")
        
obj=students()


# this is example of abstract base class 
class students(ABC):
    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def roll(self):
        pass
    
class class1(students):
    def name(self):
        print("name")
    
    def roll(self):
        print("roll")
    
        
obj=class1()
        