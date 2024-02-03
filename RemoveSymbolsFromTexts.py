from typing import List
def removeSpecialCharacters(strParam: str) -> str:
    # write your code here ^_^
    strParam1 = ""
    for i in strParam :
        if i.isalnum() or (i == '-') or (i == '_') or (i == ' ') :
            strParam1 = strParam1+ i 
    return strParam1



