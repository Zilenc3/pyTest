maxCount = 1
a = "abcabcbb" #3 abc
b = "bbbbbb" #1
c = "pwwkew" #3 wke

def EvalStr (str, x, y):
    global maxCount
    for i in range(len(str[x:y])):
        if str[-1] not in str[x:(y-1)]:
            y = y + 1
            EvalStr(str,x,y)
        else:
            if maxCount < y:
                maxCount = y - 1
                print(maxCount)
                return


def SearchStr (testStr):
    for i in range(len(testStr)):
        for j in range(len(testStr) - i):
            partialStr = testStr[i:j+2]
            EvalStr(partialStr,1,2)

SearchStr(a)