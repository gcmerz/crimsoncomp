import collections

def swapchars(word):
  letters = collections.Counter(word)
  # figure out which letter is most common
  most, _ = letters.most_common()[0]
  if most == ' ':
      most, _ = letters.most_common()[1]
  # figure out which letter is least common
  least, _ = letters.most_common()[-1]
  return word.replace(most, least)

def sortcat(num, *args):
    li = []
    for a in args:
        li.append(a)
    li.sort(key = len)
    li.reverse()
    st = ''
    if num == (-1):
        for l in li:
            st == st + l
        return st
    n = 0
    while num != 0:
        st = st + li[n]
        num = num - 1
        n = n + 1
    return st

def bluesclues(ab):
    abbrev = {}
    with open('states.txt') as f:
        lines = [line.rstrip('\n') for line in f]
        for l in lines:
            x, y = tuple(l.split(','))
            abbrev.update({y:x})
    return abbrev[ab]

def bluesbooze(name):
    abbrev = {}
    with open('states.txt') as f:
        lines = [line.rstrip('\n') for line in f]
        for l in lines:
            x, y = tuple(l.split(','))
            abbrev.update({x:y})
    return abbrev[name]
