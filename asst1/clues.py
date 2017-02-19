abbr = {}


def clues(st):
    stf = open('states.txt')
    for line in stf:
        lst = line.strip().split(',')
        abbr[lst[1]] = lst[0]
    return abbr[st]
