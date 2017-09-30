def sortcat (num, string):
	output = ""
	words = string.split()
	words = sorted(words, key=len, reverse=True)
	print num
	i = 0
	if num > 0:
		while i < num:
			output += words[i]
			i += 1
	if test == -1:
		while i < len(words):
			output += words[i]
			i += 1
	print output
	return output

string = raw_input("Strings: ")
num = raw_input("Number: ")
sortcat(num, string)