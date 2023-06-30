from typing import List
def sum_even(arr: List[int]) -> int:
    # write your code here ^_^
    sum1 = 0
    for i in range (len(arr)) :
        if arr[i] % 2 == 0 :
            sum1 = sum1 + arr[i]
    return sum1
