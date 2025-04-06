def has_unique_chars(input_string):
    """
    Checks if a string contains only unique characters without using
    additional data structures.

    Args:
        input_string: The string to check.

    Returns:
        True if all characters in the string are unique, False otherwise.
    """
    n = len(input_string)

    # If the string is empty or has only one character, it's unique.
    if n <= 1:
        return True

    # Iterate through each character using index i
    for i in range(n):
        # Compare the character at index i with all subsequent characters (index j)
        for j in range(i + 1, n):
            # If we find the same character later in the string, it's not unique
            if input_string[i] == input_string[j]:
                return False

    # If the nested loops complete without finding any duplicates, the string is unique
    return True


# --- Example Usage ---
string1 = "abcdefg"
string2 = "hello"
string3 = ""
string4 = "a"
string5 = "abcdeafg"  # 'a' is repeated
string6 = "1234567890"
string7 = "123451"    # '1' is repeated

print(f"'{string1}' has unique characters: {has_unique_chars(string1)}")
print(f"'{string2}' has unique characters: {has_unique_chars(string2)}")
print(f"'{string3}' has unique characters: {has_unique_chars(string3)}")
print(f"'{string4}' has unique characters: {has_unique_chars(string4)}")
print(f"'{string5}' has unique characters: {has_unique_chars(string5)}")
print(f"'{string6}' has unique characters: {has_unique_chars(string6)}")
print(f"'{string7}' has unique characters: {has_unique_chars(string7)}")