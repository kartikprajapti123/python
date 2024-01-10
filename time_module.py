import time

# time is used to work with time related concept like
# time.time()
def function():
    a=time.time()
    for i in range(1,10):
        print(i)
        
    b=time.time()

    c=b-a
    print(c)
function()


# time.sleep function 
def function():
    a=time.time()
    for i in range(1,10):
        print(i)
        
    time.sleep(10)
    b=time.time()

    c=b-a
    print(c)
function()


# this gives us local time 
def function():
    c=time.ctime()
    print(c)
function()