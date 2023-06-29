from typing import List
def primes_nums(numbers: List[int]) -> List[int]:
    # write your code here ^_^
    primesnums = []
    for i in range(len(numbers)):
        isPrimes = True
        for j in range(2,int(numbers[i]/2)):
            if numbers[i] % j == 0 :
                isPrimes = False
                break
        if isPrimes :
            primesnums.append(numbers[i])
    return primesnums

