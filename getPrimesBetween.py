from typing import List
def getPrimesBetween(a: int, b: int) -> List[int]:
    # write your code here ^_^
    arr = []
    if a == 1 :
        a = 2
    for i in range(a,b+1) :
        isPrimes = True
        for j in range(2,int (i/2)+1):
            if i % j == 0 :
                isPrimes = False
        if isPrimes  :
            arr.append(i)
    return arr


