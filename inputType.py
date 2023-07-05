from typing import List
def input_type(value: str) -> str:
    # write your code here ^_^
    if value.isdigit() :
        return 'integer'
    if value.replace('.','',1).isdigit() : 
        return 'double'
    return 'string'
