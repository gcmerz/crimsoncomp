from collections import Counter

def swapchars (str):
    
    str = str.lower()
    most = Counter(str).most_common(2)
    least = Counter(str).most_common()[:-1]

    
    for n in range(0,len(most)):
        if most[n][0].isalpha:
            most_let = most[n][0]
        else:
            most_let = most[0][0]

    for c in range(0,len(least)):
        if least[c][0].isalpha:
            least_let = least[c][0]
        else:
            least_let = least[0][0]

    str = str.replace(most_let, '!')
    str = str.replace(least_let, most_let)
    str = str.replace('!', least_let)
    print str

swapchars('I\'m just a chi-town coder with a nice flow.')





def sortcat(n, *args):
    tot = ''
    
    if n == -1:
        for i in args:
            tot = tot+ i
        print tot
    else:
        
        args = sorted(args, key=len)
        args = args[len(args)-1:len(args)-n-1:-1]
        for c in args:
            tot = tot + c
        print tot

sortcat(-1, 'a', 'b')
sortcat(1, 'abc', 'bc')
sortcat(2, 'bc', 'c', 'abc')



def op_rd (file):
    abbrev = {}
    with open(file) as f:
        for line in f:
            state, abb = line.rstrip().split(',', 1)
            abbrev[abb] = state
    return abbrev



def bluesclues(ab, dict):
    print dict[ab]

bluesclues('WI', op_rd('states.txt'))
bluesclues('SC', op_rd('states.txt'))

def bluesbooze (st, mydict):
    inverted_dict = dict([[v,k] for k,v in mydict.items()])
    print inverted_dict[st]

bluesbooze('Colorado', op_rd('states.txt'))
bluesbooze('Ohio', op_rd('states.txt'))



