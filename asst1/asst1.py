'''
Created on Feb 18, 2017

@author: dansoberanes
'''

import collections

def swapchars(n):
    most = collections.Counter(n.lower()).most_common(1)
    # most[0][0] will return only the most common letter
    
    least = collections.Counter(n.lower()).most_common()[:-1-1:-1]
    # least[0][0] will return only the least common letter
    
    # replace all the least common letters with most common letters
    newN = n.lower().replace(most[0][0],'\|').replace(least[0][0],most[0][0]).replace('\|',least[0][0])
    
    # loop through original word to correct capitalization in final word
    for i in range(len(n)):
        if n[i].isupper():
            newN = newN[:i]+newN[i].upper()+newN[i+1:]
            
    return newN


def sortcat(n, *args):
    # convert to list
    l = list(args)
    
    # sort in order of increasing length
    l.sort(key=len)
    
    # reverse list to be in decreasing length order
    newL = l[::-1]
    
    finalL = ""
    # if n is -1 concatenate all the string arguments
    if n == -1:
        finalL = "".join(newL)
    # otherwise concatenate all n arguments of greatest length
    else:
        for i in range(n):
            finalL += newL[i]
        
    return finalL


def bluesclues(abbv):
    # access the dictionary created from the file with the given key and return the state
    state = blueDict[abbv]
    return state


def bluesbooze(state):
    # create a list of all the key,value pairs in the dictionary
    allValues = blueDict.items()
    # iterate through each key,value pair
    for key,val in allValues:
        # if the state matches the current value, return the key for that value
        if state == val:
            return key
    return 0

# create an empty dictionary
blueDict = {}
# read through each line in the provided file
with open("states.txt") as f:
    for line in f:
        # assign values to the key and value of the dictionary by splitting the lines in the file at the comma
        (key, val) = line.split(",")
        # fill the dictionary with the key value pairs, making sure to remove the '\n' from the end of the string
        blueDict[val.strip()] = key
