import collections


def swapchars(phrase):
	most = collections.Counter(phrase).most_common()[0][0]
	least = collections.Counter(phrase).most_common()[-1][0]

	newstring = ''
	for elt in phrase:
		if elt == most:
			newstring += least
		elif elt == least:
			newstring += most
		else:
			newstring += elt

	print newstring

swapchars('I\'m just a chi-town coder with a nice flow.')

# uppercase and lowercase are considered separate, it counts spaces

def sortcat(n, *arg):
	x = list(arg)
	l = sorted(x, key=len, reverse=True)
	
	if n == -1:
		print ''.join(l)
	else:
		print ''.join(l[:n])

sortcat(1, 'abc', 'bc')
sortcat(2, 'bc', 'c', 'abc')

file = open("crimsoncomp/asst1/states.txt", "r")
contents = file.readlines()
new = [i.split(',') for i in contents]
new2 = [x[1] for x in new]
new3 = [i.split('\n') for i in new2]
abbr = [x[0] for x in new3]
names = [x[0] for x in new] 
#make separate lists for abbreviations and names and put those into dictionaries
abbrev = dict(zip(abbr, names))

print abbrev['AL']

def bluesclues(letters):

	for state in abbrev:
		if letters == state:
			print abbrev[state]

bluesclues('PA')


def bluesbooze(name):
	#print abbrev
	for state in abbrev:
		if name == abbrev[state]:
			print state

bluesbooze('Nebraska')
