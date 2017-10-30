from collections import Counter
import re

def swapchars(line):
	nline = re.sub("[^a-zA-Z]+", "", line)
	linelc = Counter(nline.lower())
	most = linelc.most_common(1)
	least = linelc.most_common(len(linelc))[len(linelc)-1]
	noli= list(line.lower().replace(most[0][0], least[0][0].upper()).replace(least[0][0], most[0][0]).replace(least[0][0].upper(), least[0][0].lower()))
	for i in xrange(len(line)):
		if line[i].isupper():
			noli[i]=noli[i].upper()
	return "".join(noli)

def sortcat(n, *args): # stole the solution from code review sorry
	s = sorted(args, key = lambda x: len(x), reverse = True)
	if n==-1:
		return "".join(s)
	return "".join(s[:n])

def bluesclues(abb):
	f = open("states.txt")
	dic = {}
	for lin in f:
		state = re.sub("\n", "", lin).split(",")
		dic[state[1]] = state[0]
	f.close()
	return dic[abb]

def bluesbooze(abb):
	f = open("states.txt")
	dic = {}
	for lin in f:
		state = re.sub("\n", "", lin).split(",")
		dic[state[0]] = state[1]
	f.close()
	return dic[abb]

print swapchars('I\'m just a chi-town coder with a nice flow.')
print sortcat(3, 'abc', 'bc', 'cd')
print bluesclues("TX")
print bluesbooze("Texas")
