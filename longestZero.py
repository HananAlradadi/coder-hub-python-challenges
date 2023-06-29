from typing import List
def longestZero(strParam: str) -> str:
    maxlenZero = ""
    i = 0
    while i < len(strParam):
        lenZero = ''
        if strParam[i] == "0":
            for j in range(i,len(strParam)):
                if not strParam[j] == "0":
                    i = j
                    if len(lenZero) > len(maxlenZero):
                        maxlenZero = lenZero
                    break
                lenZero = lenZero+'0'


        i = i +1
    return maxlenZero



    # write your code here ^_^
