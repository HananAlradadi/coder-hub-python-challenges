from typing import List
def unique(arr: List[int]) -> List[int]:
    # write your code here ^_^
    uniquearr = []
    for i in range(len(arr)):
        uniqueornot = True
        for j in range (len(arr)):
            if j != i and arr[j] == arr[i]:
                uniqueornot = False
                break
        if uniqueornot :
            uniquearr.append(arr[i])
    return uniquearr
