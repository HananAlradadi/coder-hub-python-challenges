from typing import List
def isMirrored(num: int) -> bool:
    # write your code here ^_^
    num1 = str(num)
    num2 = num1[len (num1)-1]
    for i in range (len (num1)-2 , -1 , -1) :
        num2 = num2 + num1[i]
    return num == int(num2)
        
