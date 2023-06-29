from typing import List
def average(values: List[int]) -> float:
    # write your code here ^_^
    sum1 = 0
    for i in range(len(values)):
        sum1 = sum1 + values[i]
    return sum1 / len(values)
