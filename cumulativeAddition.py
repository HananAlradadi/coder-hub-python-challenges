from typing import List
def cumulative_addition(elements_array: List[int]) -> List[int]:
    sum1 = 0 
    for i in range(len(elements_array)):
        sum1 = sum1 + elements_array[i]
    return [sum1,len(elements_array)]
