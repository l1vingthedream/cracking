''' Check if 2 words are permutarions of one another
    Does not convert upper and lower case.
'''
from collections import Counter


def isPermutation(word1: str, word2: str) -> bool:
    charCount: dict[str, int] = {}
    for c in word1:
        if c in charCount:
            charCount[c] += 1
        else:
            charCount[c] = 1

    for c in word2:
        if c not in charCount:
            return False
        charCount[c] -= 1

    for el in charCount:
        if charCount[el] != 0:
            return False
    return True


def altIsPermutation(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    return Counter(word1) == Counter(word2)


user1: str = input("Enter word 1: ")
user2: str = input("Enter word 2: ")
print("##\nis permutation: " + str(isPermutation(user1, user2)))
print("##\nis permutation(alt): " + str(altIsPermutation(user1, user2)))
