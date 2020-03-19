def min(a, b, c, d):
	list = []
	list.append(a)
	list.append(b)
	list.append(c)
	list.append(d)

	list.sort()

	return list[0]

a,b,c,d = input().split()

print(min(int(a), int(b), int(c), int(d)))	