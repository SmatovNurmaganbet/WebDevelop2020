import math

a = int(input())
b = int(input())

if a > 0 and b > 0: 
    if a==b:
        if math.floor(math.sqrt(a)) == math.sqrt(a):
            print(a)
if a < b:
    for i in range(a, b+1):
        if math.floor(math.sqrt(i)) == math.sqrt(i):
            print (i, end = ' ')
elif a < 0 and b > 0:
    for i in range(b+1):
        if math.floor(math.sqrt(i)) == math.sqrt(i):
            print (i, end = ' ')