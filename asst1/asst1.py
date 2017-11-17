#First assingment for crimson comp
#sorry I know this is ugly & I need to work on list comprehension (did it occasionally but still not that comfortable writing for loops liek that)

#I should have read the counter hint first....
#Also this version doesnt handle uppercase/lowercase
def swapchars(stringy):
    #first figure out the unique letters in stringy
    uniqueletter = []
    for i in range(0, len(stringy)):
        if stringy[i] not in uniqueletter:
            uniqueletter.append(stringy[i])
    #initialize a count array based on the number of unique letters
    lettercount = [0.0 for i in range(len(uniqueletter))]
    #count the number of unique letters
    for i in range(0, len(stringy)):
        for j in range(0, len(uniqueletter)):
            if uniqueletter[j] == stringy[i]:
                lettercount[j] = lettercount[j] + 1
    #find the highest and lowest indices of lettercount
    mostcommon = 0
    mcindex = 0
    leastcommon = 100000000000000
    lcindex = 0
    for i in range(0, len(lettercount)):
        if lettercount[i] > mostcommon:
            mostcommon = lettercount[i]
            mcindex = i
    for i in range(0, len(lettercount)):
        if lettercount[i] < leastcommon:
            leastcommon = lettercount[i]
            lcindex = i
    #convert the inital string to a list
    stringyarry = list(stringy)
    #replace the correct elements in the list according to indices
    for i in range(0, len(stringy)):
        if stringyarry[i] == uniqueletter[mcindex]:
            stringyarry[i] = uniqueletter[lcindex]
        elif stringyarry[i] == uniqueletter[lcindex]:
            stringyarry[i] = uniqueletter[mcindex]
    print(''.join(stringyarry))
swapchars("ffuuuuuuuucccckkkkkk")

def sortcat(n, *args):
    listy = []
    concatstr = ""
    newelement = ""
    #collect all the arguments
    for arg in args:
        listy.append(arg)
    #order the arguments in terms of length (highest to lowest)
    listy.sort(key = len)
    final = list(reversed(listy))
    #https://stackoverflow.com/questions/2587402/sorting-python-list-based-on-the-length-of-the-string
    #concatenate the n number of elements in the list (based on n)
    for i in range(0,n):
        newelement = final[i]
        concatstr = concatstr + newelement
    print(concatstr)    
sortcat(1, 'thebigH', 'NCSSM', 'shyteonakite', 'abc', 'qwerty', 'mridunnanda')

#take values inside states.txt file and put into dictionary
abbrev = {}
with open("states.txt") as f:
    for line in f:
        k, v = line.strip().split(',')
        abbrev[v.strip()] = k.strip()

#return the full form of any abbreviated state
def bluesclues(ab):
    print(abbrev[ab])
bluesclues('NC')

#returns the abbreviation of any full state
def bluesbooze(state):
    key = [k for k, v in abbrev.items() if state == v]
    print(key)
bluesbooze('North Carolina')
