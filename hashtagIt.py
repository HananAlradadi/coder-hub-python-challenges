from typing import List
def hashtag_it(my_array: List[str]) -> str:
    # write your code here ^_^
    word = '#'+my_array[0]
    for i in range(1,len(my_array)):
        word = word + " " + '#' + my_array[i] 
    return word
