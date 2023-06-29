from typing import List
def cumulative_sum(arr: List[int]) -> List[int]:
    sum1 = arr[0]
    for i in range(1,len(arr)):
        sum1 = sum1 + arr[i]
        arr[i] = sum1

    return arr
