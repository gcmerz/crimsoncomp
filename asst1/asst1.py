import sys
import collections
import string

def swapchars(s):
        sentence = list(s)
        c = collections.Counter()
        for letter in sentence:
                if letter in string.ascii_letters:
                        c[letter.lower()] += 1
        least_common = (c.most_common()[:-1-1:-1])[0][0]
        most_common = (c.most_common(1))[0][0]
        for i in range(0,len(sentence)):
                if (sentence[i] == sentence[i].upper()) and (sentence[i] == least_common.upper()):
                        sentence[i] = most_common.upper()
                elif (sentence[i] == sentence[i].upper()) and (sentence[i] == most_common.upper()):
                        sentence[i] = least_common.upper()
                elif (sentence[i] == least_common):
                        sentence[i] = most_common.lower()
                elif (sentence[i] == most_common):
                        sentence[i] = least_common.lower()
        print "".join(sentence)

def sortcat( _n_, *args):
    argslist = list(args);
    longestargs = []
    for i in range(0,_n_):
        longest = argslist[0];
        longestindex = 0;
        for j in range(0, len(argslist)):
            if (len(argslist[j]) > len(longest)):
                longest = argslist[j]
        longestargs.append(longest)
        argslist.remove(longest)
    print "\'" + "".join(longestargs) + "\'"

def bluesbooze(string):
    myfile = open("states.txt")
    abbrev = dict(s.split(",") for s in myfile)
    for key in abbrev:
        abbrev[key] = abbrev[key][:-1]
    print abbrev[string];

def bluesclues(string):
    myfile = open("states.txt")
    abbrev = dict(s.split(",") for s in myfile)
    newstring = string + '\n'
    for key in abbrev:
        if (abbrev[key] == newstring):
            print key;

