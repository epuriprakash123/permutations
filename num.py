from itertools import permutations
n=list(input())
l = list(permutations(n,len(n)))
for i in l:
	print(''.join(i))
