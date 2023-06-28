from typing import List
def deleteLastChar(word: str) -> str:
    # write your code here ^_^
    wordNoLast = ""
    for i in range(len(word)-1):
        wordNoLast = wordNoLast + word[i]
    return wordNoLast
