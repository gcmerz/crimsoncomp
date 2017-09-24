import string
from collections import Counter

###swapchars
def swapchars(tosort):
    mostLeast = Counter(tosort.lower().translate(None, string.punctuation))
    del mostLeast[' ']
    mostLeast = mostLeast.most_common()
    mostLeast = [mostLeast[0][0],mostLeast[-1][0],mostLeast[0][0].upper(),mostLeast[-1][0].upper()]
    switchedString = ''
    for char in tosort:
        if char == mostLeast[0]:
            char = mostLeast[1]
        elif char == mostLeast[2]:
            char = mostLeast[3]
        elif char == mostLeast[1]:
            char = mostLeast[0]
        elif char == mostLeast[3]:
            char = mostLeast[2]
        switchedString = switchedString+char
    return(switchedString)

### sortcat
def sortcat(num, tosort):
    if num >= len(tosort) or num < -len(tosort):
        print"Error: number of requested entries greater than length of list.\nHere is a result limited to the length of the list:\n"
        num = -n
    tosort=sorted(tosort,key=len,reverse=True)
    tempString =''
    stringAppend = tempString.join([a for a in tosort[0:num]])
    if num < 0: stringAppend = stringAppend+tosort[num]
    return stringAppend


import csv

def callDict(filename):
    dictionary = {}
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for ln in spamreader:
            dictionary[ln[0]] = ln[1]
            dictionary[ln[1]] = ln[0]
        return dictionary

### Blue's Clues
def abbrev(Abbreviation, filename = 'states.txt'):
    global stateDict
    try:
        return(stateDict[Abbreviation])
        print stateDict[Abbreviation]
    except:
        stateDict = callDict(filename)
        return(stateDict[Abbreviation])

### Blue's Booze

def bluesbooze(State, filename = 'states.txt'):
    global stateDict
    try:
        return(stateDict[State])
    except:
        stateDict = callDict(filename)
        return(stateDict[State])
