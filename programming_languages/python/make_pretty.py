#!/usr/local/bin/python3
# MACOSX

def header(string):
    size_of_string = len(string)
    border = "*" * size_of_string
    return(border + "\n" + string + "\n" + border)

def commands():
    border = "*" * 3
    return(border)

if __name__=="__main__":
    print(header("HEADER TEST 1 2 3"))
    print(commands(), 'test')