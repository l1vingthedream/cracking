
def isPalindromePerm(s: str) -> bool:
    if len(s) == 0:
        return False

    charCounter: dict[str, int] = {}
    for c in s:
        if c.isalpha():
            continue
        c = c.lower
        if c not in charCounter:
            charCounter[c] = 1
        else:
            charCounter[c] += 1

    oddCharCount: int = 0
    for el in charCounter:
        if (charCounter[el] % 2) == 1:
            oddCharCount += 1
    return False if oddCharCount > 1 else True


s = input("Enter a string for testing palindrome: ")
print(str(isPalindromePerm(s)))
