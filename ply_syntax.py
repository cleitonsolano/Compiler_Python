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
	''' DeclFuncVar : Tipo NOME DeclVar PVIRGULA DeclFuncVar
					| Tipo NOME ECOCHETE INT DCOCHETE DeclVar PVIRGULA DeclFuncVar
					| Tipo NOME DeclFunc DeclFuncVar
					|  '''


def p_DeclProg(p):
	'DeclProg : PROGRAMA Bloco'


def p_DeclVar(p):
	''' DeclVar : VIRGULA NOME DeclVar 
				| VIRGULA NOME ECOCHETE INT DCOCHETE DeclVar
				|  '''


def p_DeclFunc(p):
	'DeclFunc : EPAREN ListaParametros DPAREN Bloco'


def p_ListaParametros(p):
	''' ListaParametros : 
						| ListaParametrosCont '''


def p_ListaParametrosCont(p):
	''' ListaParametrosCont : Tipo NOME
							| Tipo NOME ECOCHETE DCOCHETE
							| Tipo NOME VIRGULA ListaParametrosCont
							| Tipo NOME ECOCHETE DCOCHETE VIRGULA ListaParametrosCont '''


def p_Bloco(p):
	''' Bloco : ECHAVES ListaDeclVar ListaComando DCHAVES
			| ECHAVES ListaDeclVar DCHAVES '''


def p_ListaDeclVar(p):
	''' ListaDeclVar : 
					| Tipo NOME DeclVar PVIRGULA ListaDeclVar 
					| Tipo NOME ECOCHETE INT DCOCHETE DeclVar PVIRGULA ListaDeclVar '''


def p_Tipo(p):
	''' Tipo : INT
			 | CAR '''


def p_ListaComando(p):
	''' ListaComando : Comando
					| Comando ListaComando '''


def p_Comando(p):
	''' Comando : PVIRGULA
				| RETORNE Expr PVIRGULA
				| LEIA LValueExpr PVIRGULA
				| ESCREVA Expr PVIRGULA
				| ESCREVA ASPASD NORMALSTRING ASPASD PVIRGULA
				| NOVALINHA PVIRGULA
				| SE EPAREN Expr DPAREN ENTAO Comando
				| SE EPAREN Expr DPAREN ENTAO Comando SENAO Comando
				| ENQUANTO EPAREN Expr DPAREN EXECUTE Comando
				| Bloco '''


def p_Expr(p):
	'Expr : AssignExpr'


def p_AssignExpr(p):
	''' AssignExpr : CondExpr
				| LValueExpr IGUAL AssignExpr '''


def p_CondExpr(p):
	''' CondExpr : OrExpr
				| OrExpr INTERROGACAO Expr DOISP CondExpr '''


def p_OrExpr(p):
	''' OrExpr : OrExpr OU AndExpr
			| AndExpr '''


def p_AndExpr(p):
	''' AndExpr : AndExpr E EqExpr
				| EqExpr '''


def p_EqExpr(p):
	''' EqExpr : EqExpr ATRIBUICAO DesigExpr
			   | EqExpr DIFERENTE DesigExpr
			   | DesigExpr '''


def p_DesigExpr(p):
	''' DesigExpr : DesigExpr MENOR AddExpr
				  | DesigExpr MAIOR AddExpr
				  | DesigExpr MAIORIGUAL AddExpr
				  | DesigExpr MENORIGUAL AddExpr
				  | AddExpr '''


def p_AddExpr(p):
	''' AddExpr : AddExpr MAIS MulExpr
                | AddExpr MENOS MulExpr
                | MulExpr '''


def p_MulExpr(p):
	''' MulExpr : MulExpr MULTIPLICACAO UnExpr
				| MulExpr DIVIDE UnExpr
				| MulExpr MOD UnExpr
				| UnExpr '''


def p_UnExpr(p):
	''' UnExpr : MENOS PrimExpr
			   | EXCLAMACAO PrimExpr
			   | PrimExpr '''


def p_LValueExpr(p):
	''' LValueExpr : NOME ECOCHETE Expr DCOCHETE
				   | NOME '''


def p_PrimExpr(p):
	''' PrimExpr : NOME EPAREN ListExpr DPAREN
				| NOME EPAREN DPAREN
				| NOME ECOCHETE Expr DCOCHETE
				| NOME
				| NUMERO
				| CAR
				| INT
				| EPAREN Expr DPAREN '''


def p_ListExpr(p):
	''' ListExpr : AssignExpr
				| ListExpr VIRGULA AssignExpr '''


#evita que o token de erro seja gerado e redefinirá os contadores de erros, assim facilitando identificação de prox erros
def p_erro1(t):
    parser.errok()


def p_erro2(p):
    if p:
        print(f'Syntax error em  {p.value}, na LINHA: {p.lineno}')
    else:
        print('Syntax error de EOF')
        raise SystemExit


parser = yacc.yacc()