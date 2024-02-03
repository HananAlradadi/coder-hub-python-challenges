from typing import List
def repetitions(s: str) -> int:
    # write your code here ^_^
    max1 = 0 
    for i in range (len(s)):
        nmuFr = 0 
        for j in range(i , len(s)) :
            if s[j] == s[i] :
                nmuFr = nmuFr+1
                continue
            break 
        if nmuFr > max1 :
            max1 = nmuFr
    return max1
