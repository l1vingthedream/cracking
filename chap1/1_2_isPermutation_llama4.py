def isPermutation(str1: str, str2: str) -> bool:
    """
    Checks if str1 is a permutation of str2.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        bool: True if str1 is a permutation of str2, False otherwise.
    """
    # Remove any whitespace and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # If the lengths are different, they can't be permutations
    if len(str1) != len(str2):
        return False

    # Create a dictionary to store character counts
    char_count = {}

    # Count characters in str1
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Subtract character counts for str2
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False  # char not found in str1

    # Check if all counts are zero
    for count in char_count.values():
        if count != 0:
            return False

    return True


entry1: str = input("Enter word 1: ")
entry2: str = input("Enter word 2: ")
print("##\nis permutation: " + str(isPermutation(entry1, entry2)))