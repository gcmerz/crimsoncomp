dic = {}

with open("states.txt") as file:
	for line in file:
		mylist = line.split(",")
		dic[mylist[1]] = mylist[0]

def bluesclues(abbrev):
	return dic[abbrev]


def bluesbooze(state):
	for abbrev in dic.keys():
		if dic[abbrev] == state:
			return abbrev