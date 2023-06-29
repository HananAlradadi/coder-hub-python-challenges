from typing import List
def cap_space(txt: str) -> str:
    # write your code here ^_^
    stra = 0
    txat = ""
    for i in range(len(txt)):
        
        if txt[i].isupper() :
            txat = txat+txt[stra:i]+ " "
            stra = i
    txat = txat+txt[stra:len(txt)]
    return txat.lower()
