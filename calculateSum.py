from typing import List
def calculate_sum(lst: List[int]) -> int:
    sum1 = 0 
    for i in range(len(lst)):
        if lst[i] == 7 :
            break
        sum1 = sum1 + lst[i]
    return sum1 
    # write your code here ^_^
