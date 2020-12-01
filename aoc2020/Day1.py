#! /usr/env python37

class Day1:
	def __init__(self, inputFile):
		self.target = 2020
		self.fileData = []

		with open(inputFile) as _:
			self.fileData = [
				int(data.replace('\n', '')) for data in _.readlines()
			]

	def part1(self):
		# Iterating through each value, calculating what our target value would be, then searching for it in the total dataset
		for first in self.fileData:
			# This is what value we're searching for
			second = self.target - first
			# If our value is in our dataset
			if second in self.fileData:
				# Return the product of the two values
				return first * second

	def part2(self):
		# Iterating through each value
		for first in self.fileData:
			# I chose to iterate through the set again as the set of possible two values is most likely larger then the set we're working with.
			for second in self.fileData:
				# Here we're using the same method as before, the possible numbers that make self equal our target is small, so we just look for it
				third = self.target - (first + second)
				if third in self.fileData:
					# Returning our answer
					return first * second * third