# create even number from all the number and give how much even camed
count=0
for i in range(1,10):
    if i % 2==0:
        count +=1
        print(i)
        
print("total even number",count)