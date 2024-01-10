# try except is used in python for running the programm after getting some KeyError
age=int(input("enter yout age:-"))

try:
    if age>=18:
        print("you can drive")
    else:
        print("you cannot drive")
except Exception as e:
    print(e)
    
    
# try except else 

name=input("enter name:-")

try:
    if name=="kartik":
        print("wellcome kartik")
        
    else:
        print("you are not my boss")
        
except Exception as e:
    print(e)
    
else:
    print("their is no exception")
    
    
# try except else and finally 
name=input("enter your name")

try:
    if name=="nothing":
        print("you enterend nothing")
        
    else:
        print("you enterned anything")
        
except Exception as e:
    print(e)

else:
    print("their is some thing error")
    
finally:
    print("this will either try will run or except will run ")
    
    

    
    