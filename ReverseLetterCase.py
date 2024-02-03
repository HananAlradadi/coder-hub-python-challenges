from typing import List
def reverse_case(strParam: str) -> str:
    # write your code here ^_^
    strParam1 = ""
    for i in strParam :
        if i.islower() :
            strParam1 = strParam1+ i.upper()
        else :
            strParam1 = strParam1+ i.lower()
    return strParam1


