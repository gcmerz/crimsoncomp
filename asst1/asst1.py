from collections import Counter
import string

def swapchars(input):
    new_string = ''
    for char in input.lower():
        if ((char in string.punctuation) or ' ' in char):
            new_string += ''
        else:
            new_string += char
    charslist = Counter(new_string).most_common(26)
    mostleast = [tuple[0] for tuple in (charslist[-1], charslist [0])]
    stringlist = list(input.lower())
    finalstring = ''
    for char in stringlist:
    	if (char == mostleast[-1]):
    		finalstring += mostleast[0]
    	elif (char == mostleast[0]):
    		finalstring += mostleast[-1]
    	else:
    		finalstring += char
    print(finalstring)

swapchars('I\'m just a chi-town coder with a nice flow.')
swapchars('AIIIIAIA')

def sortcat(n, *args):
	temp = list(args)
	temp.sort(key=len, reverse=True)
	newstring = ''
	if n != -1:
		for i in range(0, n):
			newstring += temp[i]
	else:
		for arg in temp:
			newstring += arg
	print(newstring)

sortcat(1, 'abc', 'bc')
sortcat(2, 'bc', 'c', 'abc')

thedict = {}
with open("states.txt") as f:
    for line in f:
    	(val, key) = line.split(',')
        thedict[str(key)] = val

def bluesclues(key):
	print thedict[key + '\n']

bluesclues('MA')

def bluesbooze(value):
	for key,values in thedict.items():
		if (value) in values:
			print(key.replace('\n', ''))

bluesbooze('California')
bluesbooze('Kentucky')