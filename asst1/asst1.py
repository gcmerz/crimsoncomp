from collections import Counter

### swapchars
def swapchars(string):
	string = string.lower()
	most_common = Counter(x for x in string if x.isalpha()).most_common()[0][0]
	least_common = Counter(x for x in string if x.isalpha()).most_common()[-1][0]
	swapped = ''
	for i in string:
		if i == most_common:
			swapped += least_common
		elif i == least_common:
			swapped += most_common
		else:
			swapped += i
	return swapped

### sortcat
def sortcat(n, *args):
	strings = list(args)
	strings.sort(key=len, reverse=True) 
	concat = ''
	for i in range(n):
		concat += strings[i]
	return concat
	
### Blue's Clues
states = {}
with open("states.txt", 'r') as file:
    for line in file:
    	(state, abbrev) = line.split(',')
    	states[abbrev.strip('\n')] = state

def bluesclues(abbrev):
	return states[abbrev]

### Blue's Booze
def bluesbooze(state):
	return [item for item in states.items() if item[1] == state][0][0]



