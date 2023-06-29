from typing import List
def missingLetter(txt: str) -> str:
    # write your code here ^_^
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    index = -1
    for i in range(len (alphabet)):
        if txt[0] == alphabet[i]:
            index = i+1
            break
    for i in range(1,len(txt)) :
        if txt[i] != alphabet[index] :
            return alphabet[index]
        index = index +1
    return 'No Missing Letter'



