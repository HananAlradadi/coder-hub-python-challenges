from typing import List
def Decimal_places(num: str) -> int:
    # write your code here ^_^
    num = num.split('.')
    if len(num) == 1 :
        return 0
    return len(num[1])
