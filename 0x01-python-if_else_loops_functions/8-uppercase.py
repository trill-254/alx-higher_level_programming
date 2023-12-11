#!/usr/bin/python3

def uppercase(s):
    """
    Prints a string in uppercase followed by a new line.

    Args:
    - s: A string

    Returns:
    - None
    """
    for char in s:
        uppercase_char = chr(ord(char) - ord('a') + ord('A')) if 'a' <= char <= 'z' else char
        print("{}".format(uppercase_char), end="")
    print()

if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
