#! /bin/env python37

# STD LIB
from sys import argv as args
from pathlib import Path

if __name__ == '__main__':
	args = ['', 2, 'inputFiles/day2_test']

# Our script requires two arguments,
#	Day to solve
#	Input filepath
# Lets check for those now
if len(args) < 3:
	raise ValueError('''Must both the day to solve and the input file

	USAGE:
		aoc2020 [day] [inputFile]
	''')

# Now checking if we have the input file
if not Path(str(args[2])).exists():
	raise FileNotFoundError(f'`{args[2]}` was not found, please provide a valid input file')

# Looks in order, lets find which class to create
day = f'Day{args[1]}'
# Finding the module and class for our day, creating an instance
solution = getattr(__import__(day), day)( Path(args[2]) )

# Everything is in order, we'll find the value by giving our filename to our object solver
print(f'''# Day {args[1]} Report:
	Part 1: {solution.part1()}
	Part 2: {solution.part2()}
''')