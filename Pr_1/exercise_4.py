# Exercise 4 Template
from ctypes import sizeof
from genericpath import getsize
import os
import string
from sys import getsizeof
from xml.dom.minidom import CharacterData

# Do not modify the file name or function header

# Return the size of the file and words ending in 's'
def get_file_info(filename):
	# Your code here

	if filename is None:
		raise TypeError("El fichero no puede ser nulo")
	if not type(filename) is str:
		raise TypeError("No has introducido una cadena")
	if not os.path.exists('./' + filename):
		raise OSError("El fichero no existe")

	size = 0
	wordlist = []

	with open(filename, 'r') as f:
		size = getsize(os.path.basename('./' + filename))
		for lines in f.readlines():
			for word in lines.split():
				if word[len(word) - 1] == 's':
					wordlist.append(word)

	# ...

	return (size, wordlist)