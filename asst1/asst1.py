import collections
import sys

def swapchars(str):
	lst = list(str.lower().replace(" ", ""))
	# counts how frequently letters come up
	count = collections.Counter(lst).most_common()
	# most common letter
	most_let = count[0][0]
	# least common letter
	least_let = count[-1][0]
	# initialized new string
	new_str = ""

	# iterates through the inputed string
	for letter in str:
		if letter.lower() == most_let:
			new_str += (least_let if letter.islower() else least_let.upper())
		elif letter.lower() == least_let:
			new_str += (most_let if letter.islower() else most_let.upper())
		else:
			new_str += (letter)
	return new_str
#list comprehension

print swapchars('I\'m just a chi-town coder with a nice flow')


def sortcat(num, *strings):
	x = num
	lst = sorted(strings, reverse=True, key=len)
	if num == -1:
		return ''.join(lst)
	else:
		return ''.join(lst[:x])
		#list splice

print sortcat(2, 'bc', 'c', 'abc')


with open("states.txt", "r") as f:
	
	d = dict([tuple(x.strip().split(',')) for x in f])

def bluesclues(state):
	for key, val in d.iteritems():
		if val == state:
			return (key)

print bluesclues("HA")

def bluesbooze(state):
	return (d[state])

print bluesbooze("Hawaii")