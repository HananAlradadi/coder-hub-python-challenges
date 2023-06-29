from typing import List
def add_five(arr: List[str]) -> List[str]:
    # write your code here ^_^
    for i in range(len(arr)):
        arr[i] = arr[i] + "5"
    return arr
