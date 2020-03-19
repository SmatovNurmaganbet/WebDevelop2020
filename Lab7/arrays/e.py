a = int(input())

list = [int(i) for i in input().split()]

same = False

for i in range(len(list)):
	if i+1<len(list):
		if list[i+1]>0 and list[i]>0 or list[i+1]<0 and list[i]<0:
			same = True
if same:
	print("YES")
else:
	print("NO")