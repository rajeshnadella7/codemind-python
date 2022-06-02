a=int(input())
fs=0
for i in range(1,a):
    if a%i==0:
        fs+=i
if fs>a:
    print("True")
else:
    print('False')