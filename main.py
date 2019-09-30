 
from ply_syntax import *
from ply_lexical import *
from ply import *

if __name__ == '__main__':

	file = open('entrada1.txt', 'r')
	data = file.read()
	file.close()

	parser.parse(data, lexer=lexer)




