from clues import abbr


def booze(st):
    new_abbr = {a: b for b, a in abbr.iteritems()}
    return new_abbr[st]
print booze('Nebraska')
