import string
a=input()
b=string.ascii_uppercase
c=0
for i in a:
    if i in b:
        c+=1
print(c)