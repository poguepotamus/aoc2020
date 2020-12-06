#! /usr/env python37

from collections import Counter

class Day6:
	def __init__(self, inputFile):
		with open(inputFile, newline='') as inFile:
			self.fileData = inFile.read().split('\r\n\r\n')

	def part1(self):
		return sum([
			len(set(group.replace('\r\n', '')))
			for group in self.fileData
		])

	def part2(self):
		total = 0
		for group in self.fileData:
			total += list(Counter(group).values()).count(group.count('\r\n') + 1)
		return total

if __name__ == '__main__':
	from pprint import pprint
	_ = Day6('inputFiles/day6')
	# pprint(_.fileData)
	pprint(_.part2())