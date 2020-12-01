#! /bin/env python37

# STD LIB
from sys import argv as args
from os import path

# Local
from Day1 import Day1

# Checking that input file was given
if len(args) != 2: # Arguments include the script name, so this is a single argument
	raise ValueError('Must include exactly one input file')
# # Checking that the file actually exists
if not path.exists(args[1]):
	raise FileNotFoundError(f'"{args[1]}" was not found')

# Everything is in order, we'll find the value by giving our filename to our object solver
day1 = Day1(args[1])
print(f'''# Day 1 Report:
	1: {day1.part1()}
	2: {day1.part2()}
''')