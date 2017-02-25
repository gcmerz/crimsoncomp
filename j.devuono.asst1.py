#swapchars
from collections import Counter

def swapchars(s):
    alphanum = filter(str.isalnum, s).lower()
        
        counter = Counter(alphanum)
        most_common_tuple = counter.most_common(1)
        most_common_letter, _ = most_common_tuple[0]
        
        least_common_tuple = counter.most_common()[:-1-1:-1]
        least_common_letter, _ = least_common_tuple[0]
        
        temp = s.replace(most_common_letter, "0").replace(most_common_letter.upper(), "1")
        swapped_move = temp.replace(least_common_letter, most_common_letter).replace(least_common_letter.upper(),
                                                                                     most_common_letter.upper())
                                                                                     swapped_final = swapped_move.replace("0", least_common_letter).replace("1", least_common_letter.upper())
                                                                                     
        return swapped_final


swapchars('I\'m just a chi-town coder with a nice flow.')

#sortcat
def sortcat(n, *args):
    longest = sorted(args, key=lambda x: len(x), reverse=True)
    if n == -1:
        return ''.join(longest)
    return ''.join(longest[:n])

print sortcat(1, 'abc', 'bc')
print sortcat(2, 'bc', 'c', 'abc')

#bluesclue and bluesbooze
f = open('states.txt', 'r')
pairs = [l.rstrip().split(',') for l in f.readlines()]
to_name = dict(map(reversed, pairs))
to_abbr = dict(pairs)

def bluesclues(abbr):
    return to_name[abbr]

def bluesbooze(name):
    return to_abbr[name]

print bluesclues('PA')
print bluesbooze('Nebraska')
