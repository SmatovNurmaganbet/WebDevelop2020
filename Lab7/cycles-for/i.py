import math
def devisors(a):
	cnt = 0
	for i in range(1,int(math.sqrt(a))+1):
		
		if a % i == 0:
			if math.sqrt(a) == i:
				cnt = cnt + 1
			else:
				cnt = cnt + 2
	return cnt

a = int(input())
print(devisors(a))