import ply.yacc as yacc
import ply.lex as lex
from ply_lexical import tokens, lexer
import arvore as ex
from copy import deepcopy

# @Aluno: Cleiton Solano S caetano

DictEscopo = dict()
DictFunc = dict()
Escope = dict()
EscopeTotal = ex.EscopoAV(None, None, None)
EscopeAtual = deepcopy(EscopeTotal)

'''
#defino a ordem de precedencia entre os tokens em cada ()
precedence = (
	('left', 'EPAREN', 'DPAREN'),
	('left', 'E', 'OU'),
	('left', 'MAIOR', 'MENOR', 'MAIORIGUAL', 'MENORIGUAL', 'IGUAL', 'DIFERENTE'),
	('left', 'MAIS', 'MENOS', ),
	('left', 'MULTIPLICACAO', 'DIVIDE'),
	('right', 'EXCLAMACAO', 'INTERROGACAO')
	)
'''

'''
Cada função aceita um único argumento p que é uma sequência
que contém os valores de cada símbulo gramatical na regra correspondente
'''

def p_Programa(p):
	'Programa : DeclFuncVar DeclProg'
	#Escope[str('global')] = p[1]
	print('entreiiiiiiiiiii')
	global EscopeTotal

def p_DeclFuncVar(p):
	'''
	DeclFuncVar : Tipo NOME DeclVar PVIRGULA DeclFuncVar
	DeclFuncVar : Tipo NOME ECOCHETE INTEIRO DCOCHETE DeclVar PVIRGULA DeclFuncVar
	DeclFuncVar : Tipo NOME DeclFunc DeclFuncVar
	DeclFuncVar :  
	'''
	global Escope
	global EscopeTotal
	global DictEscopo
	global DictFunc

	Repete = False
	flag = None
	erro = 0

	if len(p) > 5:
        #declvar e declafunvar tem as recursões

		if p[ 3 ]!=None and p[5] != None:
			elemento = p[3]
			for v in elemento:
				elemento.setTipo(str(p[1]))
				if v in DictEscopo:
					Repete = True
					break
					DictEscopo.update(elemento)
			DictEscopo.update(P[5])# guardei nesse dicionario auxiliar os dados da recursão do DeclFuncVar

		if p[3] != "[":
			flag = ex.NoTerminalAv(tipo=p[1])# vai ter um conjunto de váriaveis(da recursão) com mesmo tipo
			if p[3] != None and p[5] == None:
				elemento = p[3]# p[3] pode ser um elementos ou  conjunto de elementos do Declvar
				for v in elemento:
					elemento[v].setTipo(str(p[1]))# cada posição adicionando o tipo da var no seu  NÓ
					if valor in DictEscopo:
						Repete = True
						break
				DictEscopo.update(elemento)
				DictEscopo.update(flag)

		if p[3] == None and p[5] != None:
			DictEscopo.update(p[5])

		elif p[3] == "[":
			flag = ex.NoTerminalAv(tipo=p[1], vetor=True, tamanhoVetor=int(p[4]))# vetor=True pois vou ter um conjuntos de elementos nesse vetor onde todos devem ser do mesmo tipo
			flag.inicializavet()# atribui um nó da Árv, um vetor de valores que tenham o mesmo tipo
			
			if p[6] != None and p[8] == None:
				elemento = p[6]
				for v in elemento:
					elemento[v].setTipo(str(p[1]))
					if v in DictEscopo:
						Repete = True
						break
				DictEscopo.update(elemento)

			elif p[6] == None and p[8] != None:
				DictEscopo.update(p[8])

			elif p[6] != None and p[8] != None:
				elemento = p[6]
				for v in elemento:
					elemento[v].setTipo(str(p[1]))
					if v in DictEscopo:
						Repete = True
						break
				DictEscopo.update(elemento)
				DictEscopo.update(p[8])
        # caso tenha algum nome de var repetido
		if str(p[2]) in DictEscopo:
			erro = 1

		if erro == 1 or Repete == True:
			print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mVÁRIAVEL JÁ DECLARADA:{str(p[2])}\033[m, LINHA: {str(p.lineno(2))}')
			exit()

		else:
			DictEscopo[str(p[2])] = flag
			p[0] = DictEscopo
			EscopeTotal.setEscopo(p[0])

	elif len(p) <= 5 and len(p) > 1:# A derivação que esse elif cria uma função que será tratada mais na frente
		flag = ex.NoFuncAv(param=p[3], retorno=str(p[1]))

		if p[4] != None:# caso tenha recursão no declFuncVar, então vou ter várias funções
			var = p[4]
			var = list(var)# crio uma lista com varias funções para depois conferir se tem funções com o mesmo nome e variáveis com mesmo nome

		for v in var:
			if v in DictEscopo:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mVÁRIAVEL JÁ DECLARADA:{str(p[2])}\033[m, LINHA: {str(p.lineno(2))}')
			exit()

		DictEscopo.update(p[4])

		if p[2] in DictFunc:
			print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mFUNÇÃO JÁ EXISTENTE:{str(p[2])}\033[m, LINHA: {str(p.lineno(2))}')
			exit()

		else:
			DictFunc[str(p[2])] = flag

		p[0] = DictEscopo

	else:
		p[0] = None





def p_DeclProg(p):
	'DeclProg : PROGRAMA Bloco'


def p_DeclVar(p):
	''' 
	DeclVar : VIRGULA NOME DeclVar 
	DeclVar : VIRGULA NOME ECOCHETE INTEIRO DCOCHETE DeclVar
	DeclVar :  
	'''

	DictEscopo = dict()
	flag = None

	if len(p) > 1:
		if p[3] != "[": # variáveis que não tem vetor
			flag = ex.NoTerminalAv()

			if p[3] != None:
				DictEscopo.update(p[3])

		elif p[3] == "[":# nó de uma variável que tem vetor é diferente
			flag = ex.NoTerminalAv(vetor=True, tamanhoVetor=int(p[4]))
			flag.inicializavet()

			if p[6] != None:
				DictEscopo.update(p[6])
        # Depois que foi verificadas as recursões nos DeclVar e armazenada os dados no DictEscopo
        # verificar se há nomes de variáveis iguais
		if p[2] in DictEscopo:
			print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mVÁRIAVEL JÁ DECLARADA:{str(p[2])}\033[m, LINHA: {str(p.lineno(2))}')
			exit()
        # Caso não tenha variáveis com mesmo nome o DictEscopo(dicionario aux) = nó da arv que foi criado durante essa recursão
        # Então pode adicionar essa etapa da recursão no dicionário aux - DictEscopo
		else:
			DictEscopo[str(p[2])] = flag
        # No final todas as recursões forem guradadas no dicionário aux
        # Assim p[0] vai receber todo o escopo criado durante as recursões DictEscopo
		p[0] = DictEscopo
	else: # derivação 'epsilon'
		p[0] = None



def p_DeclFunc(p):
	'DeclFunc : EPAREN ListaParametros DPAREN Bloco'

	DictEscopo = dict()
	p4 = None

	if len(p) == 5:
		if p[2] != None:
			DictEscopo.update((p[2]))
			p4 = p[4]

			if p4['ListaDeclVar'] != None:
				for v in DictEscopo:
					if v in p4['ListaDeclVar']:
						print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mVÁRIAVEL JÁ DECLARADA:{str(p[2])}\033[m, LINHA: {str(p.lineno(2))}')
						exit()


def p_ListaParametros(p):
	''' 
	ListaParametros : 
	ListaParametros : ListaParametrosCont 
	'''
	if len(p) != 1:
		p[0] = p[1]
	else:
		p[0] = None



def p_ListaParametrosCont(p):
	''' 
	ListaParametrosCont : Tipo NOME
	ListaParametrosCont : Tipo NOME ECOCHETE DCOCHETE
	ListaParametrosCont : Tipo NOME VIRGULA ListaParametrosCont
	ListaParametrosCont : Tipo NOME ECOCHETE DCOCHETE VIRGULA ListaParametrosCont 
	'''

	DictFunc = dict()
	flag = None

	if len(p) > 5:
		flag = ex.NoTerminalAv(tipo=p[1], vetor=True)

		if p[6] != None:
			DictFunc.update(p[6])

	elif len(p) < 5:
		if len(p) > 3 and p[3] == '[':
			flag = ex.NoTerminalAv(tipo=p[1], vetor=True)

		elif len(p) > 3 and p[3] == ',':
			flag = ex.NoTerminalAv(tipo=p[1])
			if p[4] != None:
				DictFunc.update(p[4])

	elif len(p) == 3:
		flag = ex.NoTerminalAv(tipo=p[1])
	if p[2] in DictFunc:
		print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mVariável já foi declarada nos parametros:{str(p[2])}\033[m, LINHA: {str(p.lineno(2))}')
		exit()
	else:
		DictFunc[str(p[2])] = flag

	p[0] = DictFunc


def p_Bloco(p):
	'''
	Bloco : ECHAVES ListaDeclVar ListaComando DCHAVES
	Bloco : ECHAVES ListaDeclVar DCHAVES 
	'''

	global EscopeAtual

	if len(p) == 4:
		p[0] = {'ListaDeclVar': p[2], 'ListaComando': None}
		soon = ex.EscopoAV({'ListaDeclVar': p[2], 'ListaComando': p[3]}, EscopeAtual, None)
		EscopeAtual.addFilho(soon)
		EscopeAtual = deepcopy(soon)

	elif len(p) == 5:
		p[0] = {'ListaDeclVar': p[2], 'ListaComando': p[3]}
		soon = ex.EscopoAV({'ListaDeclVar': p[2], 'ListaComando': p[3]}, EscopeAtual, None)
		EscopeAtual.addFilho(soon)
		EscopeAtual = deepcopy(soon)
	
	else:
		p[0] = None

def p_ListaDeclVar(p):
	''' 
	ListaDeclVar : 
	ListaDeclVar : Tipo NOME DeclVar PVIRGULA ListaDeclVar 
	ListaDeclVar : Tipo NOME ECOCHETE INTEIRO DCOCHETE DeclVar PVIRGULA ListaDeclVar 
	'''
    
	flag = None
	DictEscopo = dict()
	Repetido = False

	if len(p) == 1:
		p[0] = None

	elif len(p) == 6:
		flag = ex.NoTerminalAv()

		if p[5] != None:
			DictEscopo.update(p[5])
		if p[3] != None:
			elemento = p[3]

			for v in elemento:
				elemento.setTipo(str(p[1]))

				if v in DictEscopo:
					Repetido = True
					break

			DictEscopo.update(elemento)

	elif len(p) == 9:
		flag = ex.NoFuncAv(tipo=str(p[1]), vetor=True, tamanhoVetor=p[4])
		flag.inicializavet()
		if p[6] != None:
			elemento = p[6]

			for v in elemento:
				elemento.setTipo(str(p[1]))

				if v in DictEscopo:
					Repetido = True
					break

			DictEscopo.update(elemento)

		if p[8] != None:
			DictEscopo.update(p[8])

	elif Repetido == True or p[1] in DictEscopo:
		print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mVariável já foi declarada nos parametros:{str(p[2])}\033[m, LINHA: {str(p.lineno(2))}')
		exit()

	else:
		DictEscopo[str(p[2])] = flag

	p[0] = DictEscopo

def p_Tipo(p):
	''' 
	Tipo : INT
	Tipo : CAR 
	'''

	if len(p) == 2:
		p[0] = p[1]


def p_ListaComando(p):
	''' 
	ListaComando : Comando
	ListaComando : Comando ListaComando 
	'''


def p_Comando(p):
	
	''' 
	Comando : PVIRGULA
	Comando : RETORNE Expr PVIRGULA
	Comando : LEIA LValueExpr PVIRGULA
	Comando : ESCREVA Expr PVIRGULA
	Comando : ESCREVA NORMALSTRING PVIRGULA
	Comando : NOVALINHA PVIRGULA
	Comando : SE EPAREN Expr DPAREN ENTAO Comando
	Comando : SE EPAREN Expr DPAREN ENTAO Comando SENAO Comando
	Comando : ENQUANTO EPAREN Expr DPAREN EXECUTE Comando
	Comando : Expr PVIRGULA
	Comando : Bloco 
	'''

	global EscopeAtual

	if len(p) == 9:
		if(type(p[3]) == bool and p[3] == True) or (type(p[3]) == int and p[3] != 0):
			p[0] = p[6]
		else:
			p[0] = p[8]

	if len(p) == 7:
		if (type(p[3]) == bool and p[3] == True) or (type(p[3]) == int and p[3] != 0):
			p[0] = p[6]
	if len(p) == 2:
		if p[1] != ";":
			EscopeAtual = deepcopy(EscopeAtual.getPai())
			p[0] = p[1]



def p_Expr(p):
	'Expr : AssignExpr'

	p[0] = p[1]


def p_AssignExpr(p):
	''' AssignExpr : CondExpr
		AssignExpr : LValueExpr IGUAL AssignExpr 
	'''

	if len(p) == 2:
		p[0] = p[1]

	if len(p) > 1:
		a1 = p[1]# armazeno LValueExpr para conferir a tipagem
		if len(p) == 4:
			a2 = p[3]# armazeno o AssingnExpr
			if p[2] == "=":
				if type(a2) == str: # portanto essa condição é satisfeita se a tipagem for correta
					if type(a1) == ex.NoTerminalAv:# caso seja um elemento de um vetor
						a1.setValor(a2)# caso a atribuição tenha o mesmo tipo de ambos os lados. Posso setar o valor de a1 com o valor de a2
						if type(a1) == 'car':# caso não seja um elemento de vetor
							a1.setValor(a2)

						elif type(aux) == ex.NoAv:
							if a1.getTipo() == 'car':
								a1.setValor(a2)

						p[1] = a1# a1 será o novo p[1] com o valor de tipagem correta associado

				if type(a2) == int: # portanto essa condição é satisfeita se a tipagem for correta
					if type(a1) == ex.NoTerminalAv:# caso seja um elemento de um vetor
						a1.setValor(a2)# caso a atribuição tenha o mesmo tipo de ambos os lados. Posso setar o valor de a1 com o valor de a2
						if type(a1) == 'int':# caso não seja um elemento de vetor
							a1.setValor(a2)

						elif type(aux) == ex.NoAv:
							if a1.getTipo() == 'int':
								a1.setValor(a2)

					p[1] = a1

				elif type(a2) == bool:
					print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mAtribuição feita com tipos inconpatíveis\033[m, LINHA: {str(p.lineno(1))}')
					exit()


def p_CondExpr(p):
	''' CondExpr : OrExpr
		CondExpr : OrExpr INTERROGACAO Expr DOISP CondExpr 
	'''

	if len(p) == 6:
		if type(p[1]) == bool and type(p[3]) == bool and type(p[5]) == bool:
			if p[1] == True:
				p[0] = p[3]

			else:
				p[0] = p[5]

		elif type(p[1]) == bool and type(p[3]) == bool and type(p[5]) == int:
			if p[1] == True:
				p[0] = p[3]
			else:
				if p[5] != 0:
					p[0] = True

				else:
					p[0] = False

		elif type(p[1]) == int and type(p[3]) == bool and type(p[5]) == bool:
			if p[1] == 0:
				p[0] = p[5]

			else:
				p[0] = p[3]

		elif type(p[1]) == bool and type(p[3]) == int and type(p[5]) == bool:
			if p[1] == True:
				if p[3] != 0:
					p[0] = True
				else:
					p[0] = True
			else:
				p[0] = p[5]

		elif type(p[1]) == int and type(p[3]) == int and type(p[5]) == bool:
			if p[1] != 0 and p[3] != 0:
				p[0] = True

			elif p[1] == 0 and p[3] == 0:
				p[0] = p[5]

			elif p[1] != 0 and p[3] == 0:
				p[0] = False

			elif p[1] == 0 and p[3] != 0:
				p[0] = p[5]

		elif type(p[1]) == bool and type(p[3]) == int and type(p[5]) == int:
			if p[3] != 0 and p[5] != 0:
				if p[1] == True:
					p[0] = True
				else:
					p[0] = True

			elif p[3] == 0 and p[5] == 0:
				if p[1] == True:
					p[0] = False
				else:
					p[0] = False

			elif p[3] != 0 and p[5] == 0:
				if p[1] == True:
					p[0] = True
				else:
					p[0] = False

			elif p[3] == 0 and p[5] != 0:
				if p[1] == True:
					p[0] = False
				else:
					p[0] = True

		elif type(p[1]) == int and type(p[3]) == bool and type(p[5]) == int:
			if p[1] != 0 and p[5] != 0:
				p[0] = p[3]

			elif p[1] == 0 and p[5] == 0:
				p[0] = False

			elif p[1] != 0 and p[5] == 0:
				p[0] = p[3]

			elif p[1] == 0 and p[5] != 0:
				p[0] = True

		elif type(p[1]) == int and type(p[3]) == int and type(p[5]) == int:
			if p[1] == 0 and p[3] == 0 and p[5] == 0:
				p[0] = False

			elif p[1] != 0 and p[3] != 0 and p[5] != 0:
				p[0] = True

			elif p[1] != 0 and p[3] == 0 and p[5] == 0:
				p[0] = False

			elif p[1] == 0 and p[3] != 0 and p[5] == 0:
				p[0] = False

			elif p[1] == 0 and p[3] == 0 and p[5] != 0:
				p[0] = True

			elif p[1] != 0 and p[3] == 0 and p[5] != 0:
				p[0] = False

			elif p[1] != 0 and p[3] != 0 and p[5] == 0:
				p[0] = True

			elif p[1] == 0 and p[3] != 0 and p[5] != 0:
				p[0] = True

		else:
			print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mUso de operador E com tipos inconpatíveis\033[m, LINHA: {str(p.lineno(1))}')
			exit()

	if len(p) == 2:
		p[0] = p[1]



def p_OrExpr(p):
	''' OrExpr : OrExpr OU AndExpr
		OrExpr : AndExpr 
	'''

	if len(p) == 4:
		if type(p[1]) == bool and type(p[3]) == bool:
			p[0] = p[1] or p[3]

		elif type(p[1]) == int and type(p[3]) == int:
			if p[1] == 0 and p[3] == 0:
				p[0] = False or False

			elif p[1] != 0 and p[3] != 0:
				p[0] = True or True

			elif p[1] != 0 and p[3] == 0:
				p[0] = True or False

			elif p[1] == 0 and p[3] != 0:
				p[0] = False or p[3]

			elif type(p[1]) == bool and type(p[3]) == int:
				if p[3] != 0:
					p[0] = p[1] or True
				else:
					p[0] = p[1] or False

			elif type(p[1]) == int and type(p[3]) == bool:
				if p[1] != 0:
					p[0] = True or p[3]
				else:
					p[0] = False or p[3]
			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mUso de operador OU com tipos inconpatíveis\033[m, LINHA: {str(p.lineno(1))}')
				exit()

	if len(p) == 2:
		p[0] = p[1]


def p_AndExpr(p):
	''' AndExpr : AndExpr E EqExpr
		AndExpr : EqExpr 
	'''

	if len(p) == 4:
		if type(p[1]) == bool and type(p[3]) == bool:
			p[0] = p[1] and p[3]

		elif type(p[1]) == int and type(p[3]) == int:
			if p[1] == 0 and p[3] == 0:
				p[0] = False and False

			elif p[1] != 0 and p[3] != 0:
				p[0] = True and True

			elif p[1] != 0 and p[3] == 0:
				p[0] = True and False

			elif p[1] == 0 and p[3] != 0:
				p[0] = False and p[3]

			elif type(p[1]) == bool and type(p[3]) == int:
				if p[3] != 0:
					p[0] = p[1] and True
				else:
					p[0] = p[1] and False

			elif type(p[1]) == int and type(p[3]) == bool:
				if p[1] != 0:
					p[0] = True and p[3]
				else:
					p[0] = False and p[3]
			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mUso de operador E com tipos inconpatíveis\033[m, LINHA: {str(p.lineno(1))}')
				exit()

	if len(p) == 2:
		p[0] = p[1]


def p_EqExpr(p):
	''' EqExpr : EqExpr ATRIBUICAO DesigExpr
		EqExpr : EqExpr DIFERENTE DesigExpr
		EqExpr : DesigExpr 
	'''

	if len(p) == 4:
        #verificação de tipagem, se for igual de ambos os lados, então est´a certo senão errado
		if p[2] == "!=":
			if (type(p[1]) == str and type(p[2]) == str) or (type(p[1]) == int and type(p[2]) == int) or (type(p[1]) == bool and type(p[2]) == bool):
				p[0] = p[1] != p[2]

			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mComparação de tipos inconpatíveis\033[m, LINHA: {str(p.lineno(1))}')
				exit()

		if p[2] == "==":
			if (type(p[1]) == str and type(p[2]) == str) or (type(p[1]) == int and type(p[2]) == int) or (type(p[1]) == bool and type(p[2]) == bool):
				p[0] = p[1] == p[2]

			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mComparação de tipos inconpatíveis\033[m, LINHA: {str(p.lineno(1))}')
				exit()
	elif len(p) == 2:
		p[0] = p[1]


def p_DesigExpr(p):
	''' DesigExpr : DesigExpr MENOR AddExpr
		DesigExpr : DesigExpr MAIOR AddExpr
		DesigExpr : DesigExpr MAIORIGUAL AddExpr
		DesigExpr : DesigExpr MENORIGUAL AddExpr
		DesigExpr : AddExpr 
	'''

	# OPERADORES RELACIONAIS MANIPULAM APENAS VALORES INTEIROS!
	if len(p) == 4:
		if p[2] == "<":
			if type(p[1]) == int and type(p[3]) == int:
				p[0] = p[1] < p[3]

			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mManipulação de valores incompatíveis no operador relacional\033[m, LINHA: {str(p.lineno(1))}')

		elif p[2] == ">":
			if type(p[1]) == int and type(p[3]) == int:
				p[0] = p[1] > p[3]

			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mManipulação de valores incompatíveis no operador relacional\033[m, LINHA: {str(p.lineno(1))}')

		elif p[2] == "<=":
			if type(p[1]) == int and type(p[3]) == int:
				p[0] = p[1] <= p[3]

			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mManipulação de valores incompatíveis no operador relacional\033[m, LINHA: {str(p.lineno(1))}')

		elif p[2] == ">=":
			if type(p[1]) == int and type(p[3]) == int:
				p[0] = p[1] >= p[3]

			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mManipulação de valores incompatíveis no operador relacional\033[m, LINHA: {str(p.lineno(2))}')

	elif len(p) == 2:
		p[0] = p[1]


def p_AddExpr(p):
	''' AddExpr : AddExpr MAIS MulExpr
        AddExpr : AddExpr MENOS MulExpr
        AddExpr : MulExpr 
    '''

	if len(p) == 4:
		if p[2] == "+":
			if type(p[1]) == int and type(p[3]) == int:
				p[0] = int(p[1] + p[3])

			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mManipulação de valores incompatíveis no operador +\033[m, LINHA: {str(p.lineno(1))}')
				exit()

		if p[2] == "-":
			if type(p[1]) == int and type(p[3]) == int:
				p[0] = int(p[1] - p[3])

			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mManipulação de valores incompatíveis no operador -\033[m, LINHA: {str(p.lineno(1))}')
				exit()

	elif len(p) == 2:
		p[0] = p[1]


def p_MulExpr(p):
	''' MulExpr : MulExpr MULTIPLICACAO UnExpr
		MulExpr : MulExpr DIVIDE UnExpr
		MulExpr : MulExpr MOD UnExpr
		MulExpr : UnExpr 
	'''

	if len(p) == 4:
		if p[2] == "*":
			if type(p[1]) == int and type(p[3]) == int:
				p[0] = int(p[1] * p[3])

			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mManipulação de valores incompatíveis no operador +\033[m, LINHA: {str(p.lineno(1))}')
				exit()

		if p[2] == "/":
			if type(p[1]) == int and type(p[3]) == int:
				if p[3] != 0:
					p[0] = int(p[1] / p[3])

				else:
					print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mOperação de divisão por ZERO -\033[m, LINHA: {str(p.lineno(3))}')
					exit()

			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mManipulação de valores incompatíveis no operador -\033[m, LINHA: {str(p.lineno(1))}')
				exit()

		if p[2] == "%":
			if type(p[1]) == int and type(p[3]) == int:
				if p[3] != 0:
					p[0] = int(p[1] % p[3])
				else:
					print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mResto da divisão utilizado com ZERO +\033[m, LINHA: {str(p.lineno(3))}')
					exit()
			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mManipulação de valores incompatíveis no operador +\033[m, LINHA: {str(p.lineno(1))}')
				exit()

	elif len(p) == 2:
		p[0] = p[1]


def p_UnExpr(p):
	''' UnExpr : MENOS PrimExpr
		UnExpr : EXCLAMACAO PrimExpr
		UnExpr : PrimExpr 
	'''

	if len(p) == 3:
		if p[1] == "!":
			if p[2] == True or p[2] == False:
				p[0] = not p[2]

			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mNegação não pode ser feita com valores inteiros +\033[m, LINHA: {str(p.lineno(2))}')
				exit()

		if p[1] == "-":
			if type(p[2]) == int:
				p[0] = - p[2]

			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mNegação SÓ pode ser feita com valores inteiros +\033[m, LINHA: {str(p.lineno(2))}')
				exit()

	if len(p) == 2:
		p[0] = p[1]


def p_LValueExpr(p):
	''' LValueExpr : NOME ECOCHETE Expr DCOCHETE
		LValueExpr : NOME 
	'''

	global Escope
	global EscopeAtual
	global EscopeTotal
	Presente = False

	if len(p) == 5:
		for v in Escope:
			if p[1] not in v:
				Presente = True

		if Presente == True:
			print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mNão declarado no escopo:{str(p[1])}\033[m, LINHA: {str(p.lineno(1))}')
			exit()

		if p[3] != None:
			p3 = p[3]
			if type(p3) != bool and p3 >= 0:
				if p[1].getTamVet() <= p3:
					print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mNão Indice não existe\033[m, LINHA: {str(p.lineno(1))}')
					exit()
				else:
					p[0] = p[1].getElemVet(t3)
			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mNão Indice não existe\033[m, LINHA: {str(p.lineno(1))}')
				exit()
		else:
			print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mNão Indice não existe\033[m, LINHA: {str(p.lineno(1))}')
			exit()

	elif len(p) == 2:
		''' for v in Escope:
            if p[1] not in v: # verificando se tem nome existente
                Presente = True'''
        #escop = deepcopy(EscopeTotal)

		if Presente == True:
			print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mNão declarado no escopo:{str(p[1])}\033[m, LINHA: {str(p.lineno(1))}')
			exit()

			p[0] = p[1]



def p_PrimExpr(p):
	''' PrimExpr : NOME EPAREN ListExpr DPAREN
		PrimExpr : NOME EPAREN DPAREN
		PrimExpr : NOME ECOCHETE Expr DCOCHETE
		PrimExpr : NOME
		PrimExpr : CCONSTANTE
		PrimExpr : INTEIRO
		PrimExpr : EPAREN Expr DPAREN 
	'''

	global EscopeAtual
	global Escope
	Presente = False
	escop = None

	if len(p) >= 4:
		if p[2] == "[":
			if p[3] != None:
				p3 = p[3]
				if type(p3) != bool:
					if p[1].getTamVet() <= p3:
						print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mIndice vet inexistente:{str(p[1])}\033[m, LINHA: {str(p.lineno(1))}')
						exit()

					else:
						p[0] = p[1].getVal(p3)

				else:
					print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mIndice vet inexistente:{str(p[1])}\033[m, LINHA: {str(p.lineno(1))}')
					exit()

			else:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mIndice vet inexistente:{str(p[1])}\033[m, LINHA: {str(p.lineno(1))}')
				exit()

		elif p[2] != "(" and p[2] != "[" and p[1]!= str and p[1] != int:
			for v in Escope:
				if p[1] not in v:
					Presente = True

			if Presente == True:
				print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mNão declarado no escopo:{str(p[1])}\033[m, LINHA: {str(p.lineno(1))}')
				exit()

			p[0] = p[1].getVal()

		for v in Escope:
			if p[1] not in v:
				Presente = True

		if Presente == True:
 			print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mNão declarado no escopo:{str(p[1])}\033[m, LINHA: {str(p.lineno(1))}')
 			exit()


def p_ListExpr(p):
	''' ListExpr : AssignExpr
		ListExpr : ListExpr VIRGULA AssignExpr 
	'''


'''

#evita que o token de erro seja gerado e redefinirá os contadores de erros, assim facilitando identificação de prox erros
def p_erro1(t):
    parser.errok()


def p_erro2(p):
    if p:
        print(f'Syntax error em  {p.value}, na LINHA: {p.lineno}')
    else:
        print('Syntax error de EOF')
        raise SystemExit


'''
parser = yacc.yacc()