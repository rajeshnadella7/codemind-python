a=int(input())
a=str(a)
a=list(a)
for i in range(0,len(a)):
    if a[i]=='6':
        a[i]='9'
        break
a=''.join(a)
print(a)