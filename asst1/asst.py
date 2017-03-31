from collections import Counter

def swapchars(str):
    lst = Counter(str).most_common()

    most_common = lst[0][0]
    least_common = lst[-1][0]

    ret = ""

    for c in str:
        if c == most_common:
            ret += least_common
        elif c == least_common:
            ret += most_common
        else:
            ret += c

    return ret

def sortcat(n, *args):
    lst = list(args)

    sortedlst = sorted(lst, key = len)

    ret = ""

    for i in range (n):
        ret += sortedlst[i]

    return ret

abbrev = {}
with open("states.txt") as f:
    for line in f:
        (value, key) = line.split(",")
        abbrev[str(key).strip("\n")] = value

def bluesclues(ab):
    return abbrev[ab]

def bluesbooze(state):
    for key, value in abbrev.items():
        if value == state:
            return key
