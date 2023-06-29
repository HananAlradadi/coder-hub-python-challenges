from typing import List
def factorial(number: int) -> int:
    # write your code here ^_^
    factorialNum = 1
    for i in range(2 , number+1):
        factorialNum = factorialNum * i
    return factorialNum
    
