from typing import List
def find_prefix(words: List[str], text: str) -> List[str]:
    # write your code here ^_^
    arr = []
    text = text.lower()
    for i in range(len(words)) :
        if words[i][0:len(text)].lower() == text :
            arr.append(words[i])
    if len(arr) == 0 :
        arr.append('No matches found')
    return arr 
