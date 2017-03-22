import collections

def swapchars(s):
  sc = collections.Counter(filter(str.isalpha,s.lower())).most_common()
  sc2 = list(s)
  most = sc[0][0]
  least = sc[len(sc)-1][0]
  print(sc)
  count = 0
  while(count < len(s)):
    if s[count] == most:
      sc2[count] = least
    elif s[count] == most.upper():
      sc2[count] = least.upper()
    elif s[count] == least:
      sc2[count] = most
    elif s[count] == least.upper():
      sc2[count] = most.upper()
    count += 1
  return ''.join(sc2)

def sortcat(*arg):
  n = arg[0]
  lst = list(arg[1:])
  lst.sort(key=len, reverse=True)
  s = ""
  if n == -1:
    s = ''.join(lst)
  else:
    count = 0
    while count < n:
      s = s + lst[count]
      count += 1
  return s

def bluesclues(s):
  d = {}
  with open("states.txt") as f:
    for line in f:
      l = line[:-1]
      (val, key) = l.split(",")
      d[key] = val
  return d[s]

def bluesbooze(s):
  d = {}
  with open("states.txt") as f:
    for line in f:
      l = line[:-1]
      (key, val) = l.split(",")
      d[key] = val
  return d[s]
