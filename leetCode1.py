
a = "abcabcbb" #3 abc
b = "bbbbbb" #1
c = "pwwkew" #3 wke

def EvalStr (str, x, y, maxCount):
    for i in range(len(str[x:y])):
        if str[-1] not in str[x:(y-1)]:
            y = y + 1
            EvalStr(str,x,y,maxCount)
        else:
            if maxCount < y:
                maxCount = y
                print(maxCount)
                return


def SearchStr (testStr):
    maxCount = 1
    for i in range(len(testStr)):
        partialStr = testStr[i:len(testStr)]
        EvalStr(partialStr,1,2, maxCount)

SearchStr(a)