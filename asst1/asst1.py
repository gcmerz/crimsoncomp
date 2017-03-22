from collections import Counter

def swapchars(string):
    common = Counter(string).most_common()
    mc = common[0][0]
    lc = common[-1][0]
    return ''.join([lc if x == mc else mc if x == lc else x for x in string])

def sortcat(n, *strs):
    strs = sorted(strs, key=len, reverse=True)
    n = len(strs) if n < 0 else n
    return ''.join(strs[:n]) 

with open('states.txt') as f:
    abbrev = dict([tuple(x.strip().split(',')) for x in f.readlines()])

def bluesclues(abbr):
    for key,value in abbrev.iteritems():
        if value == abbr:
            return key

def bluesbooze(name):
    return abbrev[name]

