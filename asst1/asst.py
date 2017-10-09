from collections import Counter

def swapchars(s):
    c = Counter()

    temp = s.replace(" ","").lower()
    common = Counter(temp).most_common(len(temp))[0][0]
    rare = Counter(temp).most_common(len(temp))[-1][0]

    s = s.replace(common, rare)
    s = s.replace(common.upper(), rare.upper())

    return s



def sortcat(n, *args):
    arr = list(args)
    arr.sort(key = lambda s: len(s))
    output = ''
    if n == -1:
        n=len(arr)

    for x in range(n):
        output += arr[len(arr)-1-x]
    return output




def bluesclues(s):
    file = open("states.txt","r")
    abbrev={}
    for line in file:
        abbrev[line[-3:].strip()] = line[:-4].strip()

    return abbrev[s]


def bluesbooze(s):
    file = open("states.txt", "r")
    abbrev = {}
    for line in file:
        abbrev[line[-3:].strip()] = line[:-4].strip()

    for x in abbrev:
        if abbrev[x] == s:
            return x

