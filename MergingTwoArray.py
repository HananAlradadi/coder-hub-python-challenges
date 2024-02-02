from typing import List
def mergeAndOrder(array1: List[int], array2: List[int]) -> List[int]:
    # write your code here ^_^
    for i in range(len(array2)):
        array1.append(array2[i])
    return sorted (array1)
