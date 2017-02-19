def sortcat(num, *argv):
    sList = []
    for arg in argv:
        sList.append(arg)
    sList.sort(key=len, reverse=True)
    s = ""
    for i in range(len(sList)):
        if i < num:
            s += sList[i]
    print s
sortcat(1, 'abc', 'c')
