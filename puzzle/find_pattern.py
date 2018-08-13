def findPattern(n):
	if n == 0:
		return 1
	else:
		return findPattern(n-1)