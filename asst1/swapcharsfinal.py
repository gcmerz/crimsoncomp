from collections import Counter

def swapchars(s):
	c = Counter(s) 
	d = c.most_common()
	mostcl = d[0][0]
	leastcl = d[-1][0]
	new_s = ""
	for char in s:
		if char == mostcl:
			new_s += leastcl
		elif char == leastcl:
			new_s += mostcl
		else:
			new_s += char
	return new_s

print swapchars("gaabbbiiii")