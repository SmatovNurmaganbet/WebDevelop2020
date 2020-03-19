n = int(input())
mas = list(map(int, input().split()))
answ = 0
for i in range (1, len(mas)):
   if mas[i] > mas[i-1]:
       answ += 1
print (answ)