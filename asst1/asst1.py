# coding: utf-8
import collections
import sys

# Return that string with the most common letter swapped with the least common letter
def swapchars(input):
	without_punc = ""
	length = len(input)
	for i in range(length):
		if input[i].isalpha():
			without_punc += input[i]
	
	char_list = collections.Counter(without_punc).most_common(26)
	input_length = len(char_list)
	most_common = char_list[0][0]
	least_common = char_list[input_length - 1][0]

	switched = ""

	for i in range(length):
		if input[i] == most_common.upper() or input[i] == most_common.lower():
			switched = switched + least_common
		elif input[i] == least_common.upper() or input[i] == least_common.lower():
			switched = switched + most_common
		else:
			switched = switched + input[i]

	return switched

# Takes one (1) integer argument n and an arbitrary number of string arguments. 
# Return the concatenation of the longest n arguments from longest to shortest. 
# If n is -1, concatenate all the arguments in this fashion
def sortcats(n, *args):
	lengths_list = []
	char_list = []
	for per in args:
		lengths_list.append(len(per))
		char_list.append(per)

	key_list = sorted(zip(lengths_list, char_list), reverse = True)

	concat = ""
	for i in range(n):
		concat += key_list[i][1]

	return concat

# Creates list of states and abbreviations
def state_list():
	state_list = []
	with open("states.txt") as f:
		for line in f:
			state_list.append(line.strip().split(","))
	return state_list

# Takes in a state abbreviation and returns the full name of the state
def bluesclues(abb): 
	slist = state_list()
	slist_length = len(slist)

	for i in range(slist_length):
		if slist[i][1] == abb:
			return slist[i][0] 

# Takes in the full name of a state and returns the state's abbreviation
def bluesbooze(fname):
	slist = state_list()
	slist_length = len(slist)

	for i in range(slist_length):
		if slist[i][0] == fname:
			return slist[i][1] 

def main():
	print swapchars('I\'m just a chi-town coder with a nice flow.')
	print sortcats(2, 'bc', 'c', 'abc')
	print bluesclues('AZ')
	print bluesbooze('California')

if __name__ == "__main__": 
	main()