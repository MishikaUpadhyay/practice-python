num= int(input("enter no. of fibonacci numbers you want to genetrate: "))
a=1
b=1
if num >= 1:
    print(a)
if num >= 2:
    print(b)
for i in range(3, num + 1):
    c = a + b
    print(c,)
    a = b
    b = c