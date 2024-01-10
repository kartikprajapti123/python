# create a program to get maximum charatcter is repeat in sentence 
sentence="hello my name is kartik how are you brother"

dic={}
for item in sentence:
    if item in dic:
        dic[item] +=1
        
    else:
        dic[item]=1
        
        
print(dic)