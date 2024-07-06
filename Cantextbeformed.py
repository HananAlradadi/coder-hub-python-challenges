from typing import List
def canForm(source: str, target: str) -> str:
    # write your code here ^_^
    txt = ""
    source = source.lower()
    target = target.lower()
    for i in target :
        if i not in source :
            return "no"
        source.replace(i, '', 1)
    return "yes"
