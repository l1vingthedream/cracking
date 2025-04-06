def urlify_string(char_array, true_length):
    """
    Replaces all spaces in a string with '%20'.

    Args:
        char_array (list): A list of characters representing the string.
        true_length (int): The true length of the string.

    Returns:
        str: The URLified string.
    """
    # Calculate the new length
    new_length = true_length
    space_count = 0
    for i in range(true_length):
        if char_array[i] == ' ':
            space_count += 1
    new_length += space_count * 2

    # Replace spaces with '%20'
    index = new_length - 1
    for i in range(true_length - 1, -1, -1):
        if char_array[i] == ' ':
            char_array[index] = '0'
            char_array[index - 1] = '2'
            char_array[index - 2] = '%'
            index -= 3
        else:
            char_array[index] = char_array[i]
            index -= 1

    return ''.join(char_array)


# Example usage
if __name__ == "__main__":
    char_array = list("Mr John Smith    ")
    true_length = 13
    print("\nBefore: " + ''.join(char_array))
    print("\nAfter: " + urlify_string(char_array, true_length))
