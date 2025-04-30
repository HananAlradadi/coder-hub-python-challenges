from typing import List
def distributeGifts(familySizes: List[int], totalGifts: List[int]) -> List[int]:
    # write your code here ^_^
    result = []
    for i in range(len(familySizes)) :
        result.append(totalGifts[i] // familySizes[i])
    return result
