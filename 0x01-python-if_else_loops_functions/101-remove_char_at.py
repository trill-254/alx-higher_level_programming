#!/usr/bin/python3

def remove_char_at(str, n):
    """
    Creates a copy of the string, removing the character at the position n.

    Args:
    - str: Input string
    - n: Position of the character to be removed

    Returns:
    - A new string with the character at position n removed
    """
    if n < 0 or n >= len(str):
        return str

    return str[:n] + str[n + 1:]

if __name__ == "__main__":
    print(remove_char_at("Best School", 3))
    print(remove_char_at("Chicago", 2))
    print(remove_char_at("C is fun!", 0))
    print(remove_char_at("School", 10))
    print(remove_char_at("Python", -2))
