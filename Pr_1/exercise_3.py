# Exercise 3 Template

# Do not modify the file name or function header

# Retuns a list with the prime numbers in the [a, b] interval
from typing import Type


def prime(a, b):
	# Your code here

	if a is None or b is None:
		raise TypeError("Los parámetros no pueden ser nulos")
	if not type(a) is int or not type(b) is int:
		raise TypeError("Los parámetros no son enteros")


	primes = []

	i = 2
	j = a
	while j != b+1:
		i = 2
		while i < j:
			if j % i == 0:
				break
			else:
				i = i+1
		if i == j:
			primes.append(j)
		j = j+1
	

	return primes
