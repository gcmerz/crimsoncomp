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

print swapchars("I\'m just a chi-town coder with a nice flow.")
