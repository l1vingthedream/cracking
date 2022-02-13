''' Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''

def isUnique(word: str) -> bool:
    charCount: dict[str,int] = {}
    for c in word:
        if c in charCount:
            return False
        charCount[c] = 1
    return True

userEntry = input("Enter word: ")
print(str(isUnique(userEntry)))