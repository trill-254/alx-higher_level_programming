#!/usr/bin/python3

def fizzbuzz():
    """
    Prints the numbers from 1 to 100 with specific replacements:
    - For multiples of three, print Fizz.
    - For multiples of five, print Buzz.
    - For multiples of both three and five, print FizzBuzz.

    Returns:
    - None
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")

if __name__ == "__main__":
    fizzbuzz()
    print("")
