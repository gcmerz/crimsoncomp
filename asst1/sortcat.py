def sortcat (number, string):
	output = ""
	string = string.split()
	string.sort(key = len)
	
	i = 0
	if number > 0:
		while i < number:
			output += string[i]
			i = i + 1
	else:
		for words in string:
			output += string[i]
			i = i + 1
	print output
	return output

number = raw_input("Integer: ")
string = raw_input("Strings: ")
sortcat(number, string)