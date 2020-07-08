#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import math
guess = 0
guesses = []
num_of_guesses = 0
print("*" * 40)
print("*" * 8, "Computer Guessing Game", "*" * 8, )
print("*" * 40)

low = int(input("Enter low number: "))
high = int(input("Enter high number: "))
max_of_guesses = int(math.log(high - low,2) + 1)
answer = int(input("Enter number between {0} and {1}.\n" \
                   "Computer will guess the number in {2} guesses.\n".format(low, high, max_of_guesses)))

def guess_a_number(lo, hi):
    return lo + ((hi - lo) // 2)

while (True):
    guess = guess_a_number(low, high)
    guesses.append(guess)
    num_of_guesses += 1
    if (guess < answer):
        #print("It is not {}. Guess higher".format(guess))
        low = guess + 1
    elif (guess > answer):
        #print("It is not {}. Guess lower".format(guess))
        high = guess - 1
    else:
        #print("Nice, you guessed it, the number is {}".format(answer))
        print("Number of guesses: ", num_of_guesses)
        print("Computer guesses were: ", guesses)
        break