upperbound = int(input('Enter an upper bound for a check: '))
print('Between 1 and', upperbound, 'there are')

perfectnum = 0
abundantnum = 0
deficientnum = 0

for j in range(1, upperbound + 1):
	properdiv = 0
	for i in range(1, j):
		if j % i == 0:
			properdiv += i

	if properdiv < j:
		deficientnum += 1
	
	elif properdiv == j:
		perfectnum += 1
	
	elif properdiv > j:
		abundantnum += 1
	
print(deficientnum, 'deficient numbers')
print(perfectnum, 'perfect numbers')
print(abundantnum, 'abundant numbers')
