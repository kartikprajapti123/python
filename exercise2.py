# create afunction in which in it if the avlue is divisable by 3 return "fizz" and divisale by 5 "fozz" if by both return "fizz fozz"

def function(n):
    if n % 3==0 and n % 5==0:
        print("fizz fozz")
        
    elif n % 3 ==0:
        print("fizz")
        
    elif n % 5==0:
        print("fozz")
        
    else:
        print(n)

function(15) 