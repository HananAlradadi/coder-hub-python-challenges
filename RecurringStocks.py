from typing import List
def arrowDuplicates(word: str) -> str:
    word1 = ''
    for i in range (len(word)):
            if word.lower().count(word[i].lower()) > 1 :
                word1 = word1 + "<"
            else :
               word1 = word1 + ">" 
    return word1
