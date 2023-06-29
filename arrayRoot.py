from typing import List
import math
def array_root(arr: List[float]) -> List[float]:
    for i in range(len(arr)):
        arr[i] = math.sqrt(arr[i])
    return arr
    # write your code here ^_^

