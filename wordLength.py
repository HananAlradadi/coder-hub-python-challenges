from typing import List
def word_length(arr: List[str]) -> List[int]:
    # write your code here ^_^
    for i in range (len(arr)) :
        arr[i] = len (arr[i])
    return arr
