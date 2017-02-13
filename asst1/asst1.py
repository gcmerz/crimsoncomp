# Assignment 1: How to Python

from collections import Counter
import sys


### swapchars
def swap(string, i, j):
  lst = list(string);
  lst[i], lst[j] = lst[j], lst[i]
  return ''.join(lst)

def swapchars(string):
  # get most and least common letters

  most = Counter(string.replace(' ', '').lower()).most_common(1)[0][0]
  least = Counter(string).most_common()[:-2:-1][0][0]

  # find index
  m = string.index(most)
  l = string.index(least)

  #swap
  return swap(string, m, l)


### sortcat
def sortcat(n, *args):
  # get argument list
  arglist = []
  for arg in args:
    arglist.append(arg)

  # sort the list
  arglist.sort(key=len)
  arglist = arglist[::-1]

  # concatenate
  if n != (-1):
    return "".join(arglist[:n])
  else:
    return "".join(arglist)




### Blue's Clues


def bluesclues(istate):
  statefile = open("state.txt", "r")
  abbrev = {}
  for line in statefile:
    k, v = line.strip().split(',')
    abbrev[v.strip()] = k.strip()

  statefile.close()


# # Blues Booze

# tests
print swapchars('I\'m just a chi-town coder with a nice flow.')
print sortcat(2, 'bc', 'c', 'abc')
print sortcat(1, 'abc', 'bc')


