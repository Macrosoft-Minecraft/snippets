import re

"""
To TKM by Federal 
More compact and faster
@TKM, thanks for the tips <3
"""
class Indenter:

	CHAR = '\t'
	SIZE = 1 #1 is the default value

	def __init__(self, code): #Pass the code its self intead of lines
		self.lines = code.split('\n')
		self.stack = [] # It stores the serching endings
		self.indented = []
		self.level = 0
		self.blocks = {
			'IF': 			['ELSEIF', 'ELSE', 'ENDIF'],
			'ELSEIF':		['ELSEIF', 'ELSE', 'ENDIF'],
			'ELSE':			['ENDIF'],
			'IFMATCHES': 	['ELSEIF', 'ELSE', 'ENDIF'],
			'IFBEGINSWITH': ['ELSEIF', 'ELSE', 'ENDIF'],
			'IFENDSWITH': 	['ELSEIF', 'ELSE', 'ENDIF'],
			'IFCONTAINS': 	['ELSEIF', 'ELSE', 'ENDIF'],
			'FOR': 			['NEXT'],
			'FOREACH':		['NEXT'],
			'DO':			['UNTIL','WHILE','LOOP'],
			'UNSAFE':		['ENDUNSAFE']
		}
		self.openings = r'{}'.format('|'.join(set([s for s in self.blocks]))) # It fetches a regex of ORs including all the openings

	def related_command(line, pattern):
		match = re.match(r'^({})\b.*'.format(pattern), line, re.IGNORECASE)
		return None if not match else match.groups()[0]

	def indent_line(self, line):
		self.indented.append(Indenter.CHAR * Indenter.SIZE * self.level + line) #Inserts a line into  the indented output list lines

	def indent(self):
		for line in self.lines:
			l = line.strip()
			closed = False

			if self.level and Indenter.related_command(l, self.stack[-1]): #Checks if the line corresponds to an ending
				self.stack.pop() 
				self.level -= 1 #Forwards the indentation
				self.indent_line(l)
				closed = True
			command = Indenter.related_command(l, self.openings) #Get tries to extract a block opening word
			if command is not None:
				self.stack.append('|'.join(self.blocks[command]))
				if not closed: #If the block was already closed, there's no reason to repeat the line
					self.indent_line(l)
				self.level += 1 #Backwards the indentation
			elif not closed:
				self.indent_line(l) #Insert a standard (no-command) line

		return '\n'.join(self.indented) # List to text