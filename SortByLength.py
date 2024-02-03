from typing import List
def sortByLength(txt: str) -> str:
    # write your code here ^_^
    listTxt = txt.split(" ")
    listTxt = sorted(listTxt, key=lambda x: (len(x), x))
    return ' '.join(listTxt)
