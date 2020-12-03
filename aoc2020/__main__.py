#! /bin/env python37

# STD LIB
from sys import argv as args
from pathlib import Path
from glob import glob

def dayReport(day, inputFile=None):
	# Default input file and day string
	inputFile = Path(f'inputFiles/day{day}') if inputFile is None else inputFile
	day = f'Day{day}'
	# Finding the module and class for our day, creating an instance
	solution = getattr(__import__(day), day)( Path(inputFile) )
	# Everything is in order, we print our results
	print(f'''# Day {day} Report:
		Part 1: {solution.part1()}
		Part 2: {solution.part2()}
	''')

# If we have three arguments, then we're given a specific day and file to run
if len(args) == 3:
	# Now checking if we have the input file
	if not Path(str(args[2])).exists():
		raise FileNotFoundError(f'`{args[2]}` was not found, please provide a valid input file')

	# Looks in order, lets find which class to create
	dayReport(args[1], args[2])

# Otherwise, we're going to give every report
else:
	for day in [file.split('.')[0][-1] for file in glob('aoc2020/Day*.py')]:
		dayReport(day)



