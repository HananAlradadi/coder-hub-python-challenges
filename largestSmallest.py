from typing import List
def largest_smallest(array_values: List[int]) -> List[int]:
    # write your code here ^_^
    maxnum = array_values[0]
    minnum = array_values[0]
    for i in range(1,len(array_values)):
        if array_values[i] > maxnum :
            maxnum =  array_values[i]
        if array_values[i] < minnum:
            minnum =  array_values[i]
    return [maxnum,minnum]

