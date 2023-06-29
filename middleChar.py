from typing import List
def middle_char(word: str) -> str:
    # write your code here ^_^
    mid = int (len(word)/2)
    if len(word) % 2 == 0 :
        return word[mid-1] + word[mid]
    return word[mid]
