import ply.yacc as yacc
from ply_lexical import tokens


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
Cada função aceita um único argumento p que é uma sequência
que contém os valores de cada símbulo gramatical na regra correspondente
'''

def p_Programa(p):
	'Programa : DeclFuncVar DeclProg'


def p_DeclFuncVar(p):
	'''
	DeclFuncVar : Tipo NOME DeclVar PVIRGULA DeclFuncVar
	DeclFuncVar : Tipo NOME ECOCHETE INTEIRO DCOCHETE DeclVar PVIRGULA DeclFuncVar
	DeclFuncVar : Tipo NOME DeclFunc DeclFuncVar
	DeclFuncVar :  
	'''


def p_DeclProg(p):
	'DeclProg : PROGRAMA Bloco'


def p_DeclVar(p):
	''' 
	DeclVar : VIRGULA NOME DeclVar 
	DeclVar : VIRGULA NOME ECOCHETE INTEIRO DCOCHETE DeclVar
	DeclVar :  
	'''


def p_DeclFunc(p):
	'DeclFunc : EPAREN ListaParametros DPAREN Bloco'


def p_ListaParametros(p):
	''' 
	ListaParametros : 
	ListaParametros : ListaParametrosCont 
	'''


def p_ListaParametrosCont(p):
	''' 
	ListaParametrosCont : Tipo NOME
	ListaParametrosCont : Tipo NOME ECOCHETE DCOCHETE
	ListaParametrosCont : Tipo NOME VIRGULA ListaParametrosCont
	ListaParametrosCont : Tipo NOME ECOCHETE DCOCHETE VIRGULA ListaParametrosCont 
	'''


def p_Bloco(p):
	'''
	Bloco : ECHAVES ListaDeclVar ListaComando DCHAVES
	Bloco : ECHAVES ListaDeclVar DCHAVES 
	'''

def p_ListaDeclVar(p):
	''' 
	ListaDeclVar : 
	ListaDeclVar : Tipo NOME DeclVar PVIRGULA ListaDeclVar 
	ListaDeclVar : Tipo NOME ECOCHETE INTEIRO DCOCHETE DeclVar PVIRGULA ListaDeclVar 
	'''


def p_Tipo(p):
	''' 
	Tipo : INT
	Tipo : CAR 
	'''


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


def p_Expr(p):
	'Expr : AssignExpr'


def p_AssignExpr(p):
	''' AssignExpr : CondExpr
		AssignExpr : LValueExpr IGUAL AssignExpr 
	'''


def p_CondExpr(p):
	''' CondExpr : OrExpr
		CondExpr : OrExpr INTERROGACAO Expr DOISP CondExpr 
	'''


def p_OrExpr(p):
	''' OrExpr : OrExpr OU AndExpr
		OrExpr : AndExpr 
	'''


def p_AndExpr(p):
	''' AndExpr : AndExpr E EqExpr
		AndExpr : EqExpr 
	'''


def p_EqExpr(p):
	''' EqExpr : EqExpr ATRIBUICAO DesigExpr
		EqExpr : EqExpr DIFERENTE DesigExpr
		EqExpr : DesigExpr 
	'''


def p_DesigExpr(p):
	''' DesigExpr : DesigExpr MENOR AddExpr
		DesigExpr : DesigExpr MAIOR AddExpr
		DesigExpr : DesigExpr MAIORIGUAL AddExpr
		DesigExpr : DesigExpr MENORIGUAL AddExpr
		DesigExpr : AddExpr 
	'''


def p_AddExpr(p):
	''' AddExpr : AddExpr MAIS MulExpr
        AddExpr : AddExpr MENOS MulExpr
        AddExpr : MulExpr 
    '''


def p_MulExpr(p):
	''' MulExpr : MulExpr MULTIPLICACAO UnExpr
		MulExpr : MulExpr DIVIDE UnExpr
		MulExpr : MulExpr MOD UnExpr
		MulExpr : UnExpr 
	'''


def p_UnExpr(p):
	''' UnExpr : MENOS PrimExpr
		UnExpr : EXCLAMACAO PrimExpr
		UnExpr : PrimExpr 
	'''


def p_LValueExpr(p):
	''' LValueExpr : NOME ECOCHETE Expr DCOCHETE
		LValueExpr : NOME 
	'''


def p_PrimExpr(p):
	''' PrimExpr : NOME EPAREN ListExpr DPAREN
		PrimExpr : NOME EPAREN DPAREN
		PrimExpr : NOME ECOCHETE Expr DCOCHETE
		PrimExpr : NOME
		PrimExpr : CCONSTANTE
		PrimExpr : INTEIRO
		PrimExpr : EPAREN Expr DPAREN 
	'''


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