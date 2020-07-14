#!/usr/local/bin/python3
#MacOSX
# Check if a number is a prime number:
## A number is prime if it is divisible by exactly 2 distinct positive numbers 1 and the number itself.
## https://www.mathsisfun.com/prime-composite-number.html
import argparse


def is_prime(n):
    for x in range(2, n + 1):
        if (x != n):
            if (n % x) == 0:
                return False
    else:
        return True


def find_prime(n):
    list_of_prime_numbers = []
    for x in range(1, n + 1):
        if is_prime(x):
            list_of_prime_numbers.append(x)
    return list_of_prime_numbers


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int)
    args = parser.parse_args()
    number = args.number

    print("PRIME TOOL")
    print("Definition: A number is prime if it is divisible by only"
          " 2 distinct positive numbers: 1 and the number itself.")
    # if is_prime(number):
    #     print("{} is a prime number.".format(number))
    # else:
    #     print("{} is not a prime number.".format(number))

   # list = find_prime(number)
    #print("List of Prime Numbers: ", ' '.join([str(num) for num in list]))

    x = 1
    i = 1
    while (x > 0):
        x /= 2
        print("Loop {}: x = {}".format(i, x))
        i += 1