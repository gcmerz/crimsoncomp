# Eliza Scharfstein
from collections import Counter 
import string

	
def swap_chars (string):
	estring = ""
	for c in string: 
		if c.isalpha(): 
			estring += c 
	# counters via https://docs.python.org/2/library/collections.html#module-collections 
	most_common = Counter(estring).most_common()[0][0]
	least_common = Counter(estring).most_common()[-1][0]
	nstring = ""
	lstring = string.lower()
	for l in lstring:
		if l == most_common: 
			nstring += least_common
		elif l == least_common: 
			nstring() +=  most_common 
		else: 
			nstring += l
	return nstring


# to call variable number of strings: http://stackoverflow.com/questions/919680/can-a-variable-number-of-arguments-be-passed-to-a-function
def sortcat (n, *strings):
	length_list = (0, 'a')
	for string in strings: 
		length_list = length_list, (len(string), string) 
	# sorting via https://wiki.python.org/moin/HowTo/Sorting
	# reverse via https://www.quora.com/How-can-I-reverse-a-list-in-python and http://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python
	med = sorted(length_list)
	final = ""
	for tup in med: 
		if n > 0: 
			final += tup[1]
			n = n - 1
	return final 	

def bluesclues (state):
	# code for reading into new dictionary with keys
	# with help from/very similar to code from http://stackoverflow.com/questions/17714571/creating-a-dictionary-from-a-txt-file-using-python 
	# and http://stackoverflow.com/questions/4803999/python-file-to-dictionary 
	# and http://stackoverflow.com/questions/14509996/creating-a-dictionary-in-python-from-a-text-file
	# and http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
	# how to strip from http://stackoverflow.com/questions/4319236/remove-the-newline-character-in-a-list-read-from-a-file
	abbrev = {}
	dictio = open ('states.txt', 'r')
	for line in dictio: 
		(val, key) = line.rstrip('\n').split(',')
		abbrev[key] = val 
	full = abbrev[state]
	return full 

def bluesbooze (state): 
	# code for reading into new dictionary with keys
	# with help from/ very similar to code from http://stackoverflow.com/questions/17714571/creating-a-dictionary-from-a-txt-file-using-python 
	# and http://stackoverflow.com/questions/4803999/python-file-to-dictionary 
	# and http://stackoverflow.com/questions/14509996/creating-a-dictionary-in-python-from-a-text-file
	# and http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
	# how to strip from http://stackoverflow.com/questions/4319236/remove-the-newline-character-in-a-list-read-from-a-file
	abbrev = {}
	dictio = open ('states.txt', 'r')
	for line in dictio: 
		(val, key) = line.rstrip('\n').split(',')
		abbrev[val] = key
	full = abbrev[state]
	return full 







