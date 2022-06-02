def ad(n):
    s=0 
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    return s
a=int(input())
while a>9:
    a=ad(a)
print(a)