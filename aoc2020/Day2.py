#! /usr/env python37

class Day2:
	def __init__(self, inputFile):
		with open(inputFile) as _:
			self.fileData = [
				[
					string.strip() for string in data.replace('\n', '').split(':')
				] for data in _.readlines()
			]

	def part1(self):
		count = 0
		for password in self.fileData:
			charCount = int(password[1].count(password[0].split(' ')[1]))
			bounds = [int(_) for _ in password[0].split(' ')[0].split('-')]
			if bounds[0] <= charCount and charCount <= bounds[1]:
				count += 1
		return count

	def part2(self):
		count = 0
		for password in self.fileData:
			positions = [int(_) for _ in password[0].split(' ')[0].split('-')]
			key = password[0].split(' ')[1]
			chars = [password[1][pos - 1] for pos in positions]
			# print(f'char = {char}| pos = {pos}| truth = {char in pos}')
			if chars.count(key) == 1:
				count += 1
		return count

if __name__ == '__main__':
	print(Day2('inputFiles/day2').part2())