from typing import List
def first_n_vowels(phrase: str, n: int) -> str:
    Vowels = ""
    leetVowels = ['u','o','i','e','a']
    lenLv = 0
    for i in range (len(phrase)):
        if phrase[i].lower() in leetVowels :
          Vowels = Vowels + phrase[i] 
          lenLv = lenLv +1
          if lenLv == n :
            return Vowels
    return 'invalid'
