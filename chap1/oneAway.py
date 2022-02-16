''' There are three types of edits that can be performed on
    strings: insert a character, remove a character, or 
    replace a character. Given two strings, write a function
    to check if they are one edit (or zero edits) away
'''
def isOneAway(s1: str, s2: str) -> bool:
    diffCt: int = 0
    long: str   = s1 if len(s2) < len(s1) else s2
    short: str  = s2 if len(s2) < len(s1) else s1

    if len(long) == len(short):
        for i in range(len(short)):
            if short[i] != long[i]:
                diffCt += 1
    elif len(long) - len(short) > 1:
        return False
    else:
        i: int = 0
        j: int = 0
        while i < len(short) and j < len(long):
            if short[i] == long[j]:
                i+=1
            else:
                diffCt+=1
            j+=1    
    return False if diffCt > 1 else True

entry1 = input("Enter word1: ")
entry2 = input("Enter word2: ")
print("Is one away: " + str(isOneAway(entry1,entry2)))