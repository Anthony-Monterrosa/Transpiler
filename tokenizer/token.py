#! /usr/bin/env python3

from sys import getsizeof as sizeof
from timeit import timeit

class Token:
	__slots__ = ['string']

	def __init__(self, string):
		self.string = string

class Tokens:
	__slots__ = ['tokens']

	def __init__(self, *tokens):
		self.tokens = tokens

class Block:
	__slots__ = ['tokens']

	def __init__(self, *tokens):
		self.tokens = tokens

	def run(self, *tuple, **map):
		pass # Compile and run c++ file
		
class Concept:
	__slots__ = ['block', 'effects']

	def __init__(self, block, *effects):
		self.block = block
		self.effects = effects

	def make_changes(self):
		pass # Execute effects

class Tokenizer:
	__slots__ = ['keywords', 'concepts']

	def __init__(self, keywords = [], concepts = []):
		self.keywords = keywords
		self.concepts = concepts

''' Keyword meanings:
	class      -> typical meaning.
	enumerate  -> compile_time alias for data.
	alias      -> alias for any identifier
	mixin      -> text-replace function with scoping.
	preprocess -> text-replace with no scoping.
'''

structures = (Token(x) for x in ('class', 'enumerate', 'alias', 'mixin', 'preprocess'))

types = (Token(x) for x in ('flag', 'u8', 'u16', 'u32', 'u64', \
        'void', 's8', 's16', 's32', 's64', \
        'none',       'r16',        'r64', \
        'string'))

qualifiers = (Token(x) for x in ('constant', 'volatile', 'compile', 'delay', 'inline'))

control = (Token(x) for x in ('if', 'else', 'for', 'in', 'with', 'when' \
          'and', 'or', 'not', \
		  'return', 'throw', 'break', 'continue'))

type_utility = (Token(x) for x in ('auto', 'type', 'cast'))

oop = (Token(x) for x in ('new', 'delete', \
      'override', 'final', 'abstract', \
      'public', 'protected', 'private')) 

compiler = (Token(x) for x in ('pragma'))

special = (Token(x) for x in (':', '    ', '\\', \
         '(', ')', '[', ']', '{', '}', '<', '>', \
         "'", '"', '#', \
         '?', '@', \
         '+', '-', '*', '/', '%', '^^', '|', '&', '^', '~'))

tokens = Tokens(*structures, *qualifiers, *control, *type_utility, *oop, *compiler, *special)

print(sizeof(tokens))