from typing import List
def exponent_x(number: int, exponent: int) -> int:
    # write your code here ^_^
    if number == 0 or number == 1 :
        return number
    ex = 1
    for i in range(exponent):
        ex = ex * number
    return ex
