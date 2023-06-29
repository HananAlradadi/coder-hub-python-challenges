from typing import List
def stringCheck(value: List[str]) -> bool:
    # write your code here ^_^
    for i in range(len(value)-1):
        if value[i] != value[i+1] :
            return False
    return True
