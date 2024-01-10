count=0
def function(number):
    if number==1:
        return 1
    else:
        return number*function(number-1)
a=function(5)
print(a)