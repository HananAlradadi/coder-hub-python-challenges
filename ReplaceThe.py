from typing import List
def replaceThe(txt: str) -> str:
    # write your code here ^_^
    if "the" not in txt.lower():
        return txt
    vowels = {"a", "e", "i", "o", "u"}
    index = txt.find("the")
    if txt[index +4 :: ].strip()[0].lower() in vowels :
        return txt[ : index] + "an" + txt[index +3 :]
    return txt[ : index] + "a" + txt[index +3 :]
