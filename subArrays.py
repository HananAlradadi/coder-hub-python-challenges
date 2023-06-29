from typing import List
def sub_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    # write your code here ^_^
    subarr = []
    for i in range(len(arr1)):
        subarr.append(arr2[i]-arr1[i])
    return subarr
