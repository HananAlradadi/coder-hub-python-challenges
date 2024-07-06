from typing import List
def countDown(number: int) -> str:
    # write your code here ^_^
    if number >= 0 : 
        countdown_list = list(range(number, number *-1, number *-1))
    else :
        countdown_list = list(range(number, 1, 1))
    return ' '.join(map(str, countdown_list))
