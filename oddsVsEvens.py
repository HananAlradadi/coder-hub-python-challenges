from typing import List
def oddsVsEvens(num: int) -> str:
    num = str(num)
    sumodd = 0 
    sumEven = 0
    for i in range(len(num)):
        numdeg = int(num[i])
        if numdeg % 2 == 0 :
            sumEven = sumEven + numdeg
        else :
            sumodd = sumodd + numdeg
    if sumEven < sumodd :
        return "odd"
    elif sumodd < sumEven :
        return "even"
    else :
        return "equal"
