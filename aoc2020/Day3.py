#! /usr/env python37

class Day3:
	def __init__(self, inputFile):
		with open(inputFile, newline='') as _:
			self.fileData = _.read().splitlines()
		self.size = [
			len(self.fileData),
			len(self.fileData[0])
		]

	def _step(self, pattern):
		self.position = [
			self.position[0] + pattern[0],
			(self.position[1] + pattern[1]) % (self.size[1]),
		]
		pass

	def tracePath(self, pattern=(1,3)):
		self.position = pattern
		path = ''
		while self.position[0] < (self.size[0]):
			path += self.fileData[self.position[0]][self.position[1]]
			self._step(pattern)
		return path.count('#')

	def part1(self):
		return self.tracePath((1, 3))

	def part2(self):
		slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
		totals = [self.tracePath(slope) for slope in slopes]
		total = 1
		for tot in totals:
			total *= tot
		return total

if __name__ == '__main__':
	from pprint import pprint

	_ = Day3('inputFiles/day3')
	print(_.part2())