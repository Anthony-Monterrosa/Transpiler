#! /usr/bin/env python3

from copy      import copy
from functools import reduce
from argparse  import ArgumentParser
from os        import getcwd as working_directory

def print_array(array, beginning_string = '', delimiter = '', end_string = ''):
	return f'''{reduce(lambda text, item: f'{text}{item}{delimiter}', array, beginning_string)}{end_string}'''

def contains(string, *characters):
	return reduce(lambda boolean, character: boolean and character in string, characters, True)

def indices(string, *texts):
	return [[index for index, text in enumerate(string) if text == condition] for condition in texts]

def delimit(string, left, right):
	left_indices, right_indices = indices(string, left)[0], indices(string, right)[0]
	output = []

	if len(left_indices) == 0: return [string]

	shallow_left_indices, shallow_right_indices = [], []
	left_index, right_index, difference = 0, 0, 1
	while left_index < len(left_indices) and right_index < len(right_indices):
		while True:
			if left_indices[left_index] > right_indices[right_index]:
				right_index += 1
			else: break

		next = False
		while True:
			try:
				if left_indices[left_index + difference] < right_indices[right_index]:
					next = True
					difference  += 1
					right_index += 1
				else: break
			except: 
				if next: 
					next = False
					right_index -= 1
					break
				else: break

		shallow_left_indices.append(left_indices[left_index])
		shallow_right_indices.append(right_indices[right_index])

		left_index  += difference
		right_index += 1
		difference   = 1

	if len(shallow_left_indices) == 0: return [string]

	output.append(string[0:shallow_left_indices[0]])
	for left_value, right_value, left_index in zip(shallow_left_indices, shallow_right_indices, range(len(shallow_left_indices))):
		output.append(delimit(string[left_value + 1:right_value], left, right))
		if left_index != len(shallow_left_indices) - 1:
			output.append(string[right_value + 1: shallow_left_indices[left_index + 1]])
	output.append(string[shallow_right_indices[-1] + 1:])

	return [x for x in output if x]
			

class Token:
	__slots__ = ['tag', 'string']

	def __init__(self, tag, string):
		self.tag    = tag
		self.string = string

class WordMatch:
	__slots__ = ['parent', 'string']

	def __init__(self, parent, string):
		self.parent = parent
		self.string = string

	def __call__(self, type):
		return \
		self.parent               if type == 'match'   else \
		self.parent.parent        if type == 'pattern' else \
		self.parent.parent.parent if type == 'lexer'   else \
		None

	def __str__(self):
		return self.string

	def match(self, string):
		for pattern in self('lexer').patterns:
			if self.string == pattern.name:
				return pattern.match(string)
		return self.string == string

class LineMatch:
	__slots__ = ['parent', 'words']

	def __init__(self, parent, string):
		self.parent = parent
		self.words  = string.split()

	@staticmethod
	def construct(string):
		words = [word.strip() for word in string.split('|')]

def test(string, left, right):
	if string.find(left):
		if string.find(right):
			.0

def main():
	print(print_array([1,4,3,6,3,4], 'start -> ', ' : ', ' <- end'))
	print(contains('dj230dfv', 'j', '3', 'v'))
	print(contains('dsafas', ';'))
	print(delimit('asd(sdf)dfs', '(', ')'), '\n\n\n')
	print(delimit('abc(de(fg)hi)jksld(me)l', '(', ')'), '\n\n\n')
	print(delimit('a)bc()fcsdf(banan)second(shelp))sdf', '(', ')'), '\n\n\n')
	print(delimit(')))bcadd()(()()))(())secondthird()((dkksfd0-)_DSs-f)))()', '(', ')'), '\n\n\n')
	print(delimit('288sdfmva$^!DAF}DSFK@FOadjkowedfn{*(%^)', 'D', 'f'), '\n\n\n')
	print(delimit('(((((()', '(', ')'))
	print(delimit('(((((())', '(', ')'))

if __name__ == '__main__':
	main()