text = open("states.txt", "r")

lst = {}
i = 0
while i < 50:
	contents = text.readline()
	lst[contents[contents.find(',') + 1 : len(contents) - 1]] = contents[0 : contents.find(',')]
	i = i + 1

def bluesbooze(abbreviation):
	print lst[abbreviation]
	return lst[abbreviation]

abbreviation = raw_input("Abbreviation: ")
bluesbooze(abbreviation)