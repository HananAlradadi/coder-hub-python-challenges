from typing import List
def hasSpace(strParam: str) -> str:
    for i in range(len(strParam)):
        if strParam[i] == ' ' :
           strParam = strParam[:i] + '#' + strParam[i + 1:]
    return strParam
    # write your code here ^_^
