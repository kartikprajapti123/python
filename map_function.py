a=[1,2,3,4,5,6,6,7,7]

b=list(map(lambda x:x ,filter(lambda x:x>4,a)))
print(b)
