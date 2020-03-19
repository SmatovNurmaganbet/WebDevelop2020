a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a==b:
    if a % 2==0:
        print(a)
else:    
    for i in range(a, b+1):
        if i%d==c and d != 0:
            print(i, end = ' ')
        i=i+1