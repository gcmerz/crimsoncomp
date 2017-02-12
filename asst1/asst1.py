from collections import Counter
import re

def swapchars(string):
    letters_string = "".join(re.findall("\w+", string))
    common = Counter(letters_string.lower()).most_common()
    most_common = common[0][0]
    least_common = common[-1][0]
    new_string = ""

    for c in string:
        if c.lower() == most_common:
            new_string += (least_common if c.islower() else least_common.upper())
        elif c.lower() == least_common:
            new_string += (most_common if c.islower() else most_common.upper())
        else:
            new_string += c

    return new_string

print swapchars('I\'m just a chi-town coder with a nice flow.')

def sortcat(*args):
    if len(args) == 1:
        return []
    else:
        n = args[0]
        strings = args[1:]
        strings = sorted(strings, reverse=True, key=len)
        if n == -1:
            return "".join(strings)
        else:
            return "".join(strings[:n])

print sortcat(1, 'abc', 'bc')
print sortcat(2, 'bc', 'c', 'abc')

states = {}
f = open('states.txt', 'r')
f = f.read()
for s in f.split('\n'):
    line = s.split(',')
    if len(line) == 2:
        states[line[1]] = line[0]

def bluesclues(abbr):
    return states[abbr]

print bluesclues('AL')

def bluesbooze(name):
    new_dict = dict((state, abbr) for abbr, state in states.iteritems())
    return new_dict[name]

print bluesbooze('Alabama')