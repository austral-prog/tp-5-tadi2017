def max_of_two(x, y):
	if x>y:
		return x
	elif x<y:
		return y
	if x==y:
		return x or y

def max_of_three(x, y, z):
	if (x>y) and (x>z):
		return x
	elif (y>x) and (y>z):
		return y
	elif (z>x) and (z>y):
		return z
	if x==y==z:
		return x or y or z
