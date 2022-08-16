n=input()
l=['a','e','o','u','i','A','E','I','O','U']
a=0
for i in n:
    if i==" ":
        print(a,end=" ")
        a=0
    elif i in l:
        a=a+1
print(a,end=" ")