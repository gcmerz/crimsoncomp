

#1. swapchars

import collections
import string 
import unittest 

def swapchars(s): 
    cnt = collections.Counter()
    for letter in s.lower(): 
        if letter.isalpha(): 
            cnt[letter] +=1 
    (mc, y) = cnt.most_common(1)[0]
    [(lc, z)] = cnt.most_common()[:-2:-1]
    lst = list(s)
    for n,i in enumerate(lst): 
        if i == mc: 
            lst[n] = lc
        else: 
            if i.lower() == mc:
                lst[n] = lc.upper()
            else: 
                if i == lc: 
                    lst[n] = mc
                else: 
                    if i.lower() == lc: 
                        lst[n] = mc.upper()
                    else: 
                        lst[n] = i
    return "".join(lst)
    

#2. sortcat

def sortcat(i, *argv): 
    lst = list(argv)
    if i == -1:
            lstf = sorted(lst, key=len)
    else: 
        lstf = sorted(lst, key=len)[-i:]
    lstf.reverse()
    return "".join(lstf)

#3. blue's clues

with open('states.txt') as f:
    abbrev = dict(reversed(line.strip().split(',',1)) for line in f)

def bluesclues(a): 
    return (abbrev[a])

#4. blue's booze
def bluesbooze(a):
    return abbrev.keys()[abbrev.values().index(a)]


# testing 

