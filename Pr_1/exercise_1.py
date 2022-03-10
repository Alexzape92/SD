# Exercise 1 Template

# Do not modify the file name or function header

# Return the sum of those parameters that contain an even number
def accum(x, y, z):
	if not type(x) is int:
		raise TypeError("Solo se permiten enteros")
	if not type(y) is int:
		raise TypeError("Solo se permiten enteros")
	if not type(z) is int:
		raise TypeError("Solo se permiten enteros")

	sum = 0
	
	if x % 2 == 0:
		print("x es par, se sumara")
		sum += x
	
	if y % 2 == 0:
		print("y es par, se sumara")
		sum += y

	if z % 2 == 0:
		print("z es par, se sumara")
		sum += z

	return sum