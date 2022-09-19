def num(a):
    if a**(1/2)==int(a**(1/2)):
        return True
    else:
        return False
a=int(input())
for i in range(a):
    x=int(input())
    print(num(x))