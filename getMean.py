from typing import List
def get_mean(arr: List[int]) -> float:
    # write your code here ^_^
    sum1 = 0
    for i in range(len(arr)):
        sum1 = sum1 + arr[i]
    return sum1 / len(arr)

