def swapchars(s):
    maxTimes, minTimes, maxChar, minChar = 0, -1, '', ''
    letterCount = {}

    # lowercase the string so characters are treated fairly
    lowercase = s.lower()

    # get the counts of all the alphabetic characters in the string
    for char in lowercase:
        if 'a' <= char <= 'z':
            if char in letterCount:
                letterCount[char] += 1
            else:
                letterCount[char] = 1
                
    # find the most/least common characters in the string
    for letter in letterCount:
        # most common character
        if letterCount[letter] > maxTimes:
            maxTimes = letterCount[letter]
            maxChar = letter

        # least common character
        if minTimes == -1 or letterCount[letter] < minTimes:
            minTimes = letterCount[letter]
            minChar = letter

    # turn the string into a list so we can edit it
    x = list(s)

    # exchange the characters in the string (keep capitalization tho)
    for i in range(len(x)):
        # replace instances of the most common character with the least
        # common character
        if x[i].lower() == maxChar:
            # if the character is capitalized, replace it with its
            # capitalized counterpart
            if not x[i] == x[i].lower():
                x[i] = minChar.upper()
            else:
                x[i] = minChar

        # do the same thing, but with the most common character
        elif char.lower() == minChar:
            if not x[i] == x[i].lower():
                x[i] = maxChar.upper()
            else:
                x[i] = maxChar

    # concatenate all the arguments of the list and return it
    return "".join(x)


def sortcat(n, *strings):
    # sort list of strings from longest to shortest
    ordered = sorted(strings)

    # make an empty string to store the concatenation
    result = ""

    # concatenate all the strings if n = -1
    if n == -1:
        for string in ordered:
            result += string

    # otherwise, concatenate only the largest n strings
    else:
        for index in range(n):
            result += ordered[index]

    return result

# create the dictionary from states.txt
dic = {}

# iterate over the lines of the states.txt file
with open("states.txt") as handle:
    for line in handle:
        # split up each line with the comma between the state and abbreviation
        parts = line.split(",")
        dic[parts[1].rstrip()] = parts[0]


def bluesclues(abbrev):
    return dic[abbrev]


def bluesbooze(state):
    # iterate over the keys of the dictionary
    for abbrev in dic:
        # if this abbreviation leads to the state we have, return it
        if dic[abbrev] == state:
            return abbrev
