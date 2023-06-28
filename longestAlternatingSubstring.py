from typing import List
def longestAlternatingSubstring(digits: str) -> str:
    maxsub = ''
    subStr = ''
    satr = 0
    end = 1
    for i in range(1,len(digits)):
        if (int(digits[i])% 2 == 0 and int(digits[i-1])% 2 == 1) or (int(digits[i])% 2 == 1 and int(digits[i-1])% 2 == 0):
            end = i
        else:
            if len(digits[satr:end+1] ) > len(maxsub) :

                maxsub = digits[satr:end+1] 
            satr = i        
    return maxsub
