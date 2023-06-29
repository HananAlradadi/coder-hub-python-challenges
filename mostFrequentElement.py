from typing import List
def most_frequent_element(arr: List[int]) -> int:
    # write your code here ^_^
    List1 = list (set(arr))
    maxFrq = -1
    indexofFrq = 0
    for i in range(len (List1)):
        sumFeq = 0 
        for j in range(len(arr)):
            if arr[j] == List1[i]:
                sumFeq = sumFeq + 1
        if sumFeq > maxFrq :
            maxFrq = sumFeq
            indexofFrq = i
    return List1[indexofFrq]
