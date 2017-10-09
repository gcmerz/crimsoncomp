def sortcat(tired):
	w = sorted(tired, key=len) #from shortest to longest

	reverse = w[::-1] # at this point you have ['abc', 'bc', 'c']
	var = ""
	for ele in reverse[0:-1]:
		var += ele

	return var # you want to see abcbc