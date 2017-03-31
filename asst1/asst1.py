from collections import Counter
from string import maketrans

dict = {}

def swapchars(str):
	final_str = ''
	most = Counter(c.lower() for c in str if c.isalpha()).most_common(1)[0][0]
	least = Counter(c.lower() for c in str if c.isalpha()).most_common()[-1][0]	
	switch_dict = {most : least, least : most}
	for char in str:
		if char == most || char == least:
			final_str += switch_dict[char]
		else:
			final_str += char
	return final_str

def sortcat(n, *args):
	str = ''
	args = list(args)
	for i in range(n):
		str += max(args, key=len)
		args.pop(args.index(max(args, key=len)))
	return str

def bluesclues(abb):
	global dict
	dict = {}
	with open("states.txt", "r") as file:
  		for line in file:
    		array.append(line)
			pair = line.split(",")
			dict[pair[1]] = pair[0]
	return dict(abb)

def bluesbooze(state):
	return dict.keys()[dict.values().index(state)]



