from typing import List
def getBiggestShared(a: List[int], b: List[int]) -> int:
    # write your code here ^_^
    max1 =  ''
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j] :
                if max1 == '' :
                    max1 = a[i]
                elif max1 < a[i] :
                    max1 = a[i]
                break
    return max1
