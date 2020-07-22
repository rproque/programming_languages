#!/usr/bin/python

import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--name')

args = parser.parse_args()

name = args.name

def happy_birthday(name):
    name = name.capitalize()
    for x in range(2):
        print ("Happy Birthday To You")
        time.sleep(1)
    print ("Happy Birthday To " + name)
    time.sleep(1)
    print ("Happy Birthday To You")
    time.sleep(1)
    for x in range(3):
        print ("Hip Hip Horray")
        time.sleep(1)

happy_birthday(name)
