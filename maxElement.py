from typing import List
def max_element(arr: List[int]) -> int:
    maxnum = arr[0]
    for i in range(1,len(arr)):
        if maxnum < arr[i] :
            maxnum = arr[i]
    return maxnum
    # write your code here ^_^
