from collections import Counter

def remove_punctuation(s):
    return "".join([c if c.isalpha() else "" for c in s])

def swapchars(s):
    c = Counter(remove_punctuation(s.replace(" ", "").lower()))
    
    most = c.most_common(1)[0][0]
    least = c.most_common()[:-2:-1][0][0]

    ret = ""

    for a in s:
        if a.lower() == most:
            ret += least if a.islower() else least.upper()
        elif a.lower() == least:
            ret += most if a.islower() else most.upper()
        else:
            ret += a

    return ret

def sortcat(n, *args):
    s = sorted([(arg, len(arg)) for arg in args], key=lambda x: x[1], reverse=True)

    words = [word for word, length in s]
    if n == -1:
        return "".join(words)

    return "".join(words[:n])

abbrev_1 = dict()
abbrev_2 = dict()
with open("states.txt", "r") as f:
    for line in f:
        name, abbreviation = line.replace("\n", "").split(",")
        abbrev_1[abbreviation] = name
        abbrev_2[name] = abbreviation

def bluesclues(abbreviation):
    return abbrev_1[abbreviation]

def bluesbooze(name):
    return abbrev_2[name]