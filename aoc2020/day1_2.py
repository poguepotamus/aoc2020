#! /usr/env python37

from sys import argv as args
from os import path

# Checking that input file was given
if len(args) != 2: # Arguments include the script name, so this is a single argument
	raise ValueError('Must include exactly one input file')
# # Checking that the file actually exists
if not path.exists(args[1]):
	raise FileNotFoundError(f'"{args[1]}" was not found')

# Now we know the file is valid, let's get to processing
target = 2020
fileData = []
with open(args[1]) as inFile:
	fileData = [int(data.replace('\n', '')) for data in inFile.readlines()]

