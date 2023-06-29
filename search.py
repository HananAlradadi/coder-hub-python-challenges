from typing import List
def search(word: str, character: str) -> int:
    # write your code here ^_^
    for i in range(len(word)) :
        if word[i] == character :
            return i
    return -1
