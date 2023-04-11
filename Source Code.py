import random 
names=  input("Enter names seprated by commas")
namelist= names.split(",")
print(namelist)
x=len(namelist)
y=random.randint(0,x-1)
print(y)
d=(namelist[y])
print(d,"is selected")
