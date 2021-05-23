''' Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''
def isUnique(word):
    charmap = {}
    for c in word:
        charmap[c] = charmap.get(c, 0) + 1
    for el in charmap:
        if charmap[el] > 1:
            return False
    return True

str = input("Enter word: ")
print("Does the word consist of unique characters...")
print(isUnique(str))