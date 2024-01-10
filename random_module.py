import random


# this is function of random.choice
def func1():
    a=['1ksd',1,23,"msd"]
    b=random.choice(a)
    
    print(b)
    
func1()

# this is function of random.choices 
def func2():
    a=['1ksd',1,23,"msd","kasd",12,4,5,6,7,8,9,9]
    b=random.choices(a,k=2)
    
    print(b)
    
func2()


# This is function of random.randint

def func3():
    b=random.randint(1,10)
   
    print(b)
    
func3()

# this is the use of function random.random() 
def func3():
    b=random.random()
   
    print(b)
    
func3()