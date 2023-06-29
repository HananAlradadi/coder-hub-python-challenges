from typing import List
def addStrNums(num1: str, num2: str) -> str:
    # write your code here ^_^
    if num1.isnumeric() and num2.isnumeric() :
        return str(int(num1)+int(num2))
    return '-1'
