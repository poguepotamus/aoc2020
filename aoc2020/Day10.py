#! /usr/env python37

class Day10:
	def __init__(self, inputFile):
		with open(inputFile, newline='') as inFile:
			self.fileData = [int(line) for line in inFile.read().splitlines()]
			self.fileData.sort()

	def part1(self):
		# One, two, and three jolt jumps
		joltCount = [0, 0, 1]
		maxJolts = 0

		for jolts in self.fileData:
			if jolts > maxJolts + 3:
				break

			joltCount[jolts - maxJolts - 1] += 1
			maxJolts = jolts
		return joltCount[2] * joltCount[0]

	def part2(self):
		pass

if __name__ == '__main__':
	from pprint import pprint
	_ = Day10('inputFiles/day10')
	# pprint(_.fileData)
	pprint(_.part1())