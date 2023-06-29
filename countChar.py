from typing import List
def count_char(sentence: str, ch: str) -> int:
    # write your code here ^_^
    sum1 = 0 
    for i in range(len(sentence)) :
        if sentence[i] == ch :
            sum1 = sum1 + 1
    return sum1
