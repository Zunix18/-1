from math import factorial
from collections import Counter

def count_anagrams(word):
    word = word.lower()  
    total = factorial(len(word))
    counts = Counter(word)
    for freq in counts.values():
        total //= factorial(freq)
    return total


word = input("Введіть слово: ")
print("Кількість анаграм:", count_anagrams(word))
