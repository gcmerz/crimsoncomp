def swapchars(phrase):
    import collections
    onlyalpha= ''.join(c for c in phrase if c.isalpha())
    onlyalpha=onlyalpha.lower()
    m_common=collections.Counter(onlyalpha).most_common(1)
    l_common=collections.Counter(onlyalpha).most_common()[:-2:-1]
    new_phrase=""
    for i in range(0, len(phrase)):
      if phrase[i] is m_common[0][0]:
          new_phrase += l_common[0][0]
      elif phrase[i] == m_common[0][0].upper():
          new_phrase += l_common[0][0].upper()
      elif phrase[i] is l_common[0][0]:
          new_phrase += m_common[0][0]
      elif phrase[i] == l_common[0][0].upper():
          new_phrase += m_common[0][0].upper()
      else:
          new_phrase += phrase[i]
    return new_phrase

def sortcat(n, *args):
    new_list=sorted(args, key=len, reverse=True)
    outputstring=""
    if n is -1:
        for i in new_list:
            outputstring+=new_list[i]
    else:
        for i in range(0, n):
            outputstring+=new_list[i]
    return outputstring

states_dict={}
with open("states.txt") as f:
    for line in f:
        (val, key) = line.split(",")
        states_dict[key.strip("\n")] = val

def bluesclues(abbrev):
    print states_dict[abbrev]
    return states_dict[abbrev]

def bluesbooze(name):
    for key, val in states_dict.items():
        if val == name:
            return key
