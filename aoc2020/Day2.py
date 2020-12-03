#! /usr/env python37

class Day2:
	def __init__(self, inputFile):
		with open(inputFile) as _:
			self.fileData = [
				data.replace('\n', '').split(':') for data in _.readlines()
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
			char = password[0].split(' ')[1]
			pos = [password[1][pos - 1] for pos in positions]
			# print(f'char = {char}| pos = {pos}| truth = {char in pos}')
			if char in pos:
				count += 1
		return count
