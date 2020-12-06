#! /usr/env python37

class Day9:
	def __init__(self, inputFile):
		self.preambleSize = 25
		with open(inputFile, newline='') as inFile:
			self.fileData = [int(value) for value in inFile.read().splitlines()]

	def hasSum(self, target, preamble):
		for candidate in preamble:
			solution = target - candidate
			if solution in preamble:
				return True
		return False


	def part1(self):
		for index, target in enumerate(self.fileData):
			if index <= self.preambleSize:
				continue
			preamble = self.fileData[index - self.preambleSize:index]
			if not self.hasSum(target, preamble):
				return target
		return "All values have passed"

	def part2(self):
		solution = self.part1()
		crack = 0
		startIndex = 0
		endIndex = 1
		while crack != solution:
			# Adjusting range to see if we can get a match
			if crack < solution:
				# print('    Smaller')
				endIndex += 1
			else: # If crack > solution
				# print('    Larger')
				startIndex += 1

			if endIndex - startIndex < 1:
				endIndex += 1


			collection = self.fileData[startIndex:endIndex+1]
			crack = sum(collection)
			if crack == 0:
				break
			# print(f'Checking collection[{startIndex}, {endIndex}] - sum({collection}) <?> {crack} == {solution}')
		# Assuming that there will always be a solution
		# print(f'start,end = {startIndex}, {endIndex} = {self.fileData[startIndex]}, {self.fileData[endIndex]}')
		return max(self.fileData[startIndex:endIndex]) + min(self.fileData[startIndex:endIndex])

if __name__ == '__main__':
	from pprint import pprint
	_ = Day9('inputFiles/day9')
	pprint(_.part2())