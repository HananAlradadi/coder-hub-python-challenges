from typing import List
def countdown(num: int) -> List[int]:
    # write your code here ^_^
    if num <= 3 :
        return [0]
    arr = []
    while num > 3 :
        num = num - 3
        if num % 2 == 0 :
            arr.insert(0,num)
    return arr 
