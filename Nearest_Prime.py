def  prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c=c+1
    if c==2:
        return True 
    else:
        return False
def nxt_prime(a):
    while prime(a)==False:
        a=a+1
    return a
def pre_prime(a):
    while prime(a)==False:
        a=a-1
    return a
def near_prime(a):
    x=nxt_prime(a)
    y=pre_prime(a)
    if x-a>=a-y:
        print(y)
    else:
        print(x)
a=int(input())
for i in range (a):
    j=int(input())
    near_prime(j)