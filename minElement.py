from typing import List
def smallest_number(arr: List[int]) -> int:
    # write your code here ^_^
    min1 = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < min1 :
            min1 = arr[i]
    return min1
