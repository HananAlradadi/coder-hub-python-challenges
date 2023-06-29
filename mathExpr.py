from typing import List
def math_expr(expr: str) -> bool:
    # write your code here ^_^
    mathexpr = ['+','-','/','*']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    return (expr[0] in numbers) and (expr[1]in mathexpr) and (expr[2] in numbers)
