from typing import List
def str_len_comparison(words: List[str]) -> bool:
    # write your code here ^_^
    if len(words) == 1 :
        return False
    for i in range (len(words)-1):
        if not (len(words[i]) == len (words[i+1])):
            return False
    return True
    
