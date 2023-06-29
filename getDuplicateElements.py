from typing import List
def get_duplicate_elements(arr: List[int]) -> List[int]:
    # write your code here ^_^
    arr1 = []
    for i in range(len(arr)):
        if arr[i] not in arr1 :
            for j in range(i+1,len(arr)):
                if arr[i] == arr[j] :
                    arr1.append(arr[i])
                    break
    return arr1
