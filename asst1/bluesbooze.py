text = open("states.txt", "r")

lst = {}
i = 0
while i < 50:
	contents = text.readline()
	lst[contents[0 : contents.find(',')]] = contents[contents.find(',') + 1 : len(contents) - 1]
	i = i + 1

def bluesbooze(state):
	print lst [state]
	return lst [state]

state = raw_input("State: ")
bluesbooze(state)