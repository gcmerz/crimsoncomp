import collections
import string

def swapchars (w) :
  temp_str = w.translate(None, string.punctuation)
  temp_str = temp_str.translate(None, " ")
  freq = collections.Counter(temp_str.lower()).most_common()
  most, num = freq[0]
  least, num1 = freq[len(freq) - 1]
  print most
  print least
  ret = ""
  for c in w :
    if c == most.upper() :
      ret += least.upper()
    elif c == most.lower() :
      ret += least.lower()
    elif c == least.upper() :
      ret += most.upper()
    elif c == least.lower() :
      ret += most.lower()
    else :
      ret += c
  return ret

def sortcat (n, *args) :
  xs = []
  str = ""
  i = n
  for a in args :
    xs.append(a)
  xs = sorted(xs, key=len)
  for a in xs :
    if i > 0 :
      str += xs[i]
      i-=1
  if n == -1 :
    for a in reversed(xs) :
      str += a
  return str

def bluesclues (abbr) :
  f = open('states.txt')
  answer = {}
  for line in f :
    k, v = line.strip().split(',')
    answer[v.strip()] = k.strip()
  return answer[abbr]

def bluesbooze (name) :
  f = open('states.txt')
  answer = {}
  for line in f :
    k, v = line.strip().split(',')
    answer[k.strip()] = v.strip()
  return answer[name]

# tests
print swapchars('I\'m just a chi-town coder with a nice flow.')
print sortcat(-1, 'abc', 'abcd', 'helloooo')
print sortcat(1, 'abc', 'bc')
print sortcat(2, 'bc', 'c', 'abc')
print bluesclues("AL")
print bluesbooze("Nebraska")
