from typing import List
def filp_even_odd(numbers: List[int]) -> List[int]:
    # write your code here ^_^
    for i in range(len (numbers)) :
        if numbers[i] % 2 == 0 :
            numbers[i] = numbers[i] + 1
        else :
            numbers[i] = numbers[i] -1
    return numbers
