# opening file is used for making changes in the file 
file=open("content.txt","r")
f=file.read()
print(f)

# opening file is also used for append
file=open("content.txt","+a")
file.write("hello my name is gauat")
# print(f)

#opening file is also used writing
file=open("content.txt","w")
file.write("old content get old") 



#file_handling file is also used writing and reading file
file=open("content.txt","r+")
a=file.read()
print(a)
file.write("new content get old") 



#file_handling file is also used writing and reading file
file=open("content.txt","w+")
a=file.read()
print(a)
file.write("new content get old") 
