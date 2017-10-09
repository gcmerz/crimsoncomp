from collections import Counter

def swapchars(text):
	cnt = Counter(text)
	mostCommon=cnt.most_common(1)[0][0].lower()
	leastCommon=cnt.most_common(len(list(cnt)))[len(list(cnt))-1][0][0].lower()
	returnText = ''
	for elmt in text:
		if elmt == mostCommon:
			returnText = returnText + leastCommon
		elif elmt  == mostCommon.capitalize():
			returnText = returnText + leastCommon.capitalize()
		elif elmt == leastCommon:
			returnText = returnText + mostCommon
		elif elmt == leastCommon.capitalize():
			returnText = returnText + mostCommon.capitalize() 
		else:
			returnText = returnText + elmt
	print(returnText)

def sortcat(n, *tstrings):
	finalList = [tstrings[0]]
	strings = list(tstrings)
	strings.pop(0)
	for elmt in strings:
		notIn = True
		if len(elmt) > len(finalList[i]):
			finalList.insert(i,elmt)
			notIn = True
			if len(finalList)>n:
				finalList.pop(-1)
			break
		if notIn and len(finalList)<n:
			finalList.insert(len(finalList),elmt)
	finalString = ''
	for arg in finalList:
		finalString = finalString + arg
	print(finalString)

abbrev={}
file = open('states.txt','r')
content = file.readlines()
for state in content:
	mapping = state.split(",")
	mapping[1]=mapping[1][:2]
	abbrev[mapping[1]]=mapping[0]

def bluesclues(abbreviation):
	return abbrev[abbreviation]

def bluesbooze(state):
	for key,value in abbrev.iteritems():
		if value == state:
			return key

