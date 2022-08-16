a=input()
b='aeiouAEIOU'
c=0
d=0
e=0
for i in a:
    if i==' ':
        d=c
        c=0
    elif i in b:
        c+=1
        e=c
print(max(d,e))