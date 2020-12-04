#! /usr/env python37

from re import match

class Passport:
	def __init__(self, string):
		for key, value in dict(field.split(':') for field in string.strip().split(' ')).items():
			setattr(self, key, value)
		self.fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

	def fieldsValid(self):
		return sum([
			1 if field in self.__dict__ else 0
			for field in self.fields
		]) == len(self.fields)

	def inRange(self, lower, number, upper):
		return lower <= int(number) and int(number) <= upper

	def heightValid(self, height):
		cmCheck = 'cm' in height and self.inRange(150, height[:-2], 193)
		inCheck = 'in' in height and self.inRange(59,  height[:-2], 76)
		return cmCheck or inCheck

	def isValid(self):
		# First, lets check if the keys are valid
		if not self.fieldsValid():
			return False

		# Next, all the fields
		validFields = [
			self.inRange(1920, self.byr, 2002),
			self.inRange(2010, self.iyr, 2020),
			self.inRange(2020, self.eyr, 2030),
			bool(match(r'#[a-fA-F0-9]{6}', self.hcl)),
			bool(match(r'\d{9}', self.pid)) and len(self.pid) == 9,
			self.ecl in ['amb','blu','brn','gry','grn','hzl','oth'],
			self.heightValid(self.hgt),
		]
		return all(validFields)

class Day4:
	def __init__(self, inputFile):
		with open(inputFile, newline='') as inFile:
			self.fileData = [_.replace('\r\n', ' ') for _ in ''.join(inFile.read()).split('\r\n\r\n')]

	def part1(self):
		return sum([ Passport(passport).fieldsValid() for passport in self.fileData ])

	def part2(self):
		return sum([ Passport(passport).isValid() for passport in self.fileData ])

if __name__ == '__main__':
	from pprint import pprint
	_ = Day4('inputFiles/day4')

	pprint(_.part2())