#!/usr/local/bin/python3
#MACOSX
# Description: Read a file and write to another file line by line

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source_file')
parser.add_argument('-d', '--destination_file')
args = parser.parse_args()

source_file = args.source_file
destination_file = args.destination_file

reader = open(source_file, 'r')
writer = open(destination_file, 'w')
for line in reader:
    print((line.rstrip()).title())
    writer.write(line)
writer.close()
reader.close()