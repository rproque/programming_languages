#!/usr/local/bin/python3
#MacOSX

import math
guess = 0
guesses = []
num_of_guesses = 0
print("*" * 40)
print("*" * 8, "Computer Guessing Game", "*" * 8, )
print("*" * 40)

low = int(input("Enter low number: "))
high = int(input("Enter high number: "))
if (low == high):
    print("Too easy, its {}!".format(low))
    exit(0)
elif (low > high):
    print("Can't trick me, low is now {} and high is now {}".format(high, low))
    temp = low
    low = high
    high = temp
max_of_guesses = int(math.log(high - low,2) + 1)
print("Write your number down, I will guess the number in {0} guesses.\n".format(max_of_guesses))

def guess_a_number(lo, hi):
    return lo + ((hi - lo) // 2)

while (True):
    guess = guess_a_number(low, high)
    guesses.append(guess)
    num_of_guesses += 1
    high_low = input("I guess {0}.  Enter c (correct), h (higher), l (lower)".format(guess))
    if (high_low == 'h'):
        low = guess + 1
    elif (high_low == 'l'):
        high = guess - 1
    else:
        print("See! I told you I can guess the number in {} guesses!".format(max_of_guesses))
        print("Number of guesses: ", num_of_guesses)
        print("Computer guesses were: ", guesses)
        break