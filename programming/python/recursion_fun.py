#!/usr/local/bin/python3
#rules of recursion
# 1) the function needs to have a return where it stops calling it self (base case)
# 2) the function is moving towards its base case
# 3) the function returns a call to itself
import make_pretty
print('hello')
#https://en.wikipedia.org/wiki/Factorial
#the factorialorial of a positive integer n, denoted by n!, 
#is the product of all positive integers less than or equal to n:
def factorial_recursive(n):
    if n <= 1:
        return 1
    return (n * factorial_recursive(n - 1))
    
    
def factorial_iterative(n):
    result = 1
    if n > 1:
        for x in range(2, n + 1):
            result = result * x
    return(result)

#https://en.wikipedia.org/wiki/Fibonacci_number
#In mathematics, the Fibonacci numbers, commonly denoted Fn, 
#form a sequence, called the Fibonacci sequence, such that each 
#number is the sum of the two preceding ones, starting from 0 and 1. 
def fib_recursive(n):
    # F0 = 0
    if n < 2:
        return n
    else:
        return (fib_recursive(n - 1) + fib_recursive(n - 2))

def list_sum_recursive(list):
    position = len(list) - 1
    if len(list) == 1:
        return list
    else:
        new_list = []
        sum = list[position] + list[position - 1]
        for x in range(0, len(list) - 2):
            new_list.append(list[x])
        new_list.append(sum)
        return list_sum_recursive(new_list)

def list_sum_for_loop(list):
    z = 0
    for y in list:
        z += y
    return z

if __name__ == "__main__":    
#    lo,hi = 0, 7
#    print(make_pretty.header("factorial_recursive"))
#    for x in range(lo,hi):
#        print(x, factorial_recursive(x))
    
#    print(make_pretty.header("factorial_iterative"))
#    for x in range(lo,hi):
#       print(x, factorial_iterative(x))

    # print(make_pretty.header("fib_recursive"))
    # for x in range(9):
    #     print(x, fib_recursive(x))

    print(make_pretty.header("list_sum_recursive"))
    for x in range(1, 20, 2):
        print('*' * 100)
        list_to_sum = [*range(0,x,2)]
        print("list_to_sum", list_to_sum)
        print("Sum:                 ", sum(list_to_sum))
        print("For Loop:            ", list_sum_for_loop(list_to_sum))
        print("list_sum_recursive:  ", (list_sum_recursive(list_to_sum))[0])
        print('*' * 100)
