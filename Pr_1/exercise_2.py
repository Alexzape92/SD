# Exercise 2 Template

# Do not modify the file name or function header

# Adds e to mylist and returns the resulting list
from multiprocessing.sharedctypes import Value
from queue import Empty


def list_add(mylist, e):
	if e is None:
		raise TypeError("e no puede ser nulo")

	mylist.append(e)

	return mylist
	

# Removes the first occurrence of e in mylist and returns the resulting list 
def list_del(mylist, e):
	if e is None:
		raise TypeError("e no puede ser nulo")
	if mylist == []:
		raise TypeError("La lista no puede ser nula")
	
	mylist.remove(e)

	return mylist


# Adds the tuple t (value, key) to mydict and returns the resulting dictionary
def dict_add(mydict, t):
	if t is None:
		raise TypeError("t no puede ser nulo")
	if not type(t) is tuple:
		raise TypeError("t no es una tupla de dos elementos")
	
	mydict[t[0]] = t[1]
	return mydict