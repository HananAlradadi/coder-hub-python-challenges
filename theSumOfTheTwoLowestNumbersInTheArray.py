from typing import List
def sum_two_smallest_nums(arr: List[int]) -> int:
    # write your code here ^_^
    if arr[0]< arr[1] :
        min1 = arr[0]
        min2 = arr[1]
    else :
        min2 = arr[0]
        min1 = arr[1]
    
    for i in range(2,len(arr)):
        if arr[i] < min1 :
            min1 = arr[i]
        elif arr[i] < min2  :
            min2 = arr[i]   
    return min1 + min2
