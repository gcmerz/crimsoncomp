### swapchars
from collections import Counter
import string
from string import maketrans

def swapchars(message):
    messagelower = (message.lower()).replace(" ", "")
    counterstring = messagelower.translate(None, string.punctuation)
    cnt = Counter(counterstring).most_common()
    # swapping respective lower and uppercase most common & least common letters
    intab = cnt[0][0] + cnt[0][0].upper() + cnt[-1][0] + cnt[-1][0].upper()
    outtab = cnt[-1][0] + cnt[-1][0].upper() + cnt[0][0] + cnt[0][0].upper()
    trantab = maketrans(intab, outtab)
    return message.translate(trantab)

### sortcat
def sortcat(n, *args):
    result = ""
    # sort string arguments from shortest to longest
    sortedargs = sorted(args, key = len)
    # print out n longest arguments, concatenated together
    for i in range(0, n):
        result = result + sortedargs[-(i + 1)]
    return result

### Blue's Clues
abbrev = {}

with open("states.txt") as f:
    for line in f:
        row = line.strip()
        value, key = row.split(",")
        abbrev[key] = value

def bluesclues(query):
    return abbrev[query]

### Blue's Booze
def bluesbooze(query):
    for key in abbrev:
        if abbrev[key] == query:
            return key
