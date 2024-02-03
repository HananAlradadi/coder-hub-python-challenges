from typing import List
def remove_duplicate(arr: List[int]) -> List[int]:
    # write your code here ^_^
    arr2 = []
    for i in range(len(arr)):
        if arr[i] not in arr2 :
            arr2.append(arr[i])
    return arr2


