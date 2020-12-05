#! /usr/env python37

class Day5:
	def __init__(self, inputFile):
		with open(inputFile, newline='') as inFile:
			self.fileData = inFile.read().splitlines()
		self.findSeatIDs()

	def toBit(self, string):
		string = string.upper()
		string = string.replace('B', '1').replace('R', '1')
		string = string.replace('F', '0').replace('L', '0')
		return string

	def findSeatIDs(self):
		self.seatIDs = []
		for seat in self.fileData:
			seatBit = self.toBit(seat)
			row = int(seatBit[:7], 2)
			column = int(seatBit[-3:], 2)
			self.seatIDs.append(row*8 + column)

	def part1(self):
		return max(self.seatIDs)

	def part2(self):
		# Finding our range
		for num in range(min(self.seatIDs), max(self.seatIDs)):
			if num not in self.seatIDs:
				return num

if __name__ == '__main__':
	from pprint import pprint
	_ = Day5('inputFiles/day5')
	print(_.part2())