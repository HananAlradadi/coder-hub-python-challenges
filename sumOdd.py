from typing import List
def sumOdd(arr: List[int]) -> int:
    # write your code here ^_^
    sumOddNum = 0
    for i in range(len(arr)) :
        if arr[i] % 2 != 0 :
            sumOddNum = sumOddNum + arr[i]
    return sumOddNum
