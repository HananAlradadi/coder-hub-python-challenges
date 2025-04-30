from typing import List
def findDonationTargetDay(donations: List[float], target: float) -> int:
    # write your code here ^_^
    sum1 = 0 
    for i in range (len(donations)) :
        sum1 += donations[i]
        if sum1 >= target :
            return i + 1 
    
    return -1
