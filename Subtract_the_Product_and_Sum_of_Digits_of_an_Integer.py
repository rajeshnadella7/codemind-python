a=int(input())
c=1
d=0
while a>0:
    x=a%10
    c*=x
    d+=x
    a=a//10
print(c-d)