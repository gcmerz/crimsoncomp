from collections import Counter

def swapchars(string_thing):
    # initialize a counter and count each letter's occurrence
    count = Counter()
    for c in string_thing.lower():
        if c.isalpha():
            count[c] += 1

    # create a most and least common character
    char_most = count.most_common()[0][0]
    char_least = count.most_common()[-1][0]

    # initialize the new string we're going to add to
    new_string = ""

    # go through the original string and add the appropriate character
    for c in string_thing:
        if c.lower() == char_most:
            if c.isupper():
                new_string += char_least.upper()
            else:
                new_string += char_least
        elif c.lower() == char_least:
            if c.isupper():
                new_string += char_most.upper()
            else:
                new_string += char_most
        else:
            new_string += c
    return new_string

print(swapchars('I\'m just a chi-town coder with a nice flow.'))

def sortcat(n, *args):
    # initialize a list and add the elements of the args tuple
    ls = list()
    for el in args:
        ls.append(el)

    # sort the list in descending order by length of element
    ls.sort(key=lambda s : -len(s))

    # special case check and use
    if n == -1:
        n = len(ls)

    # initialize a string and add n elements to it
    s = ''
    for i in range(n):
        s += ls[i]

    return s
print(sortcat(2, 'bc', 'c', 'abc'))

def bluesclues(abb):
    # open the file and read the lines into a list
    with open('states.txt', mode='r') as f:
        states = f.readlines()

    # initialize a dictionary and add states
    state_dict = dict()
    for state in states:
        # split each line from file by comma
        s = state.split(',')

        # create a key with the abbreviation
        # create a value based on the name
        state_dict[s[1].strip()] = s[0]

    return state_dict[abb.upper()]
print(bluesclues('Ca'))

def bluesbooze(statename):
    # open the file and read the lines into a list
    with open('states.txt', mode='r') as f:
        states = f.readlines()

    # initialize a dictionary and add states
    state_dict = dict()
    for state in states:
        # split each line from file by comma
        s = state.split(',')

        # create a key with the abbreviation
        # create a value based on the name
        state_dict[s[0].lower()] = s[1].strip()
    return state_dict[statename.lower()]
print(bluesbooze('HawaII'))

# Thanks guys!
#################################
########    #######    ##########
####### #### ##### #### #########
####### ##### ### ##### #########
######## ###### ###### ##########
######### ########### ###########
########## ######### ############
########### ####### #############
############ ##### ##############
############# ### ###############
############## # ################
############### #################
#################################