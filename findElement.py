from typing import List
def find_element(elements_array: List[int], element: int) -> bool:
    # write your code here ^_^
    for i in range(len (elements_array)):
        if elements_array[i] == element :
            return True
    return False
