#! /usr/env python37

class DayN:
	def __init__(self, inputFile):
		with open(inputFile, newline='') as inFile:
			self.fileData = inFile.read().splitlines()

	def part1(self):
		pass

	def part2(self):
		pass

if __name__ == '__main__':
	from pprint import pprint
	_ = DayN('inputFiles/dayN_test')
	pprint(_.part1())
	pprint(_.part2())