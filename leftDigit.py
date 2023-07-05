from typing import List
def left_digit(strParam: str) -> int:
    # write your code here ^_^
    for i in range(len(strParam)) :
        try :
            num = int(strParam[i])
            return num
        except : 
            pass
