# is s1 a substring of s2
def is_rotation(s1: str, s2: str) -> bool:
    s1 = s1 + s1
    return True if s2 in s1 else False


s1: str = input("Enter word1: ")
s2: str = input("Enter word2: ")
print("Is String Rotation: ", is_rotation(s1, s2))
