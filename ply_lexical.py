import sys
sys.path.append("../..")

from ply import *
from ply.lex import TOKEN

'''
PALAVRAS RESERVADAS
'''

reservados = {
    'programa'  : 'PORGRAMA',
    'car'       : 'CAR',
    'int'       : 'INT',
    'retorne'   : 'RETORNE',
    'leia'      : 'LEIA',
    'escreva'   : 'ESCREVA',
    'novalinha' : 'NOVALINHA',
    'se'        : 'SE',
    'entao'     : 'ENTAO',
    'senao'     : 'SENAO',
    'enquanto'  : 'ENQUANTO',
    'execute'   : 'EXECUTE'
}

tokens = ('NOME', 'NUMERO', 'MAIS', 'MENOS', 'MULTIPLICACAO', 'DIVIDE', 'ATRIBUICAO',
          'EPAREN', 'DPAREN', 'ECOCHETE', 'DCOCHETE', 'ECHAVES', 'DCHAVES', 'VIRGULA', 'PVIRGULA',
          'OU', 'E', 'EXCLAMACAO', 'INTERROGACAO', 'DOISP', 'IGUAL', 'DIFERENTE', 'MENOR', 'MAIOR',
          'MENORIGUAL', 'MAIORIGUAL', 'ATRIBUISUM', 'ATRIBUISUB', 'ATRIBUIMULT', 'ATRIBUIDIV',
          'MOD') + tuple(reservados.values()) 

'''
TOKENS E SIMBULOS
( ) [ ] { } , ; + - * / == != > >= < <= || && ! = += -= *= /= %= ? :
'''

t_ignore        = ' \t'


t_EPAREN        = r'\)'
t_DPAREN        = r'\('
t_ECOCHETE      = r'\]'
t_DCOCHETE      = r'\['
t_ECHAVES       = r'\}'
t_DCHAVES       = r'\{'


t_VIRGULA      = r','
t_PVIRGULA      = r';'
t_OU 			= r'\|\|'
t_E             = r'&&'
t_EXCLAMACAO    = r'!'
t_INTERROGACAO  = r'\?'
t_DOISP         = r':'


t_IGUAL		    = r'=='
t_DIFERENTE		= r'!='
t_MENOR			= r'<'
t_MAIOR			= r'>'
t_MENORIGUAL    = r'<='
t_MAIORIGUAL    = r'>='

t_ATRIBUISUM    = r'\+='
t_ATRIBUISUB    = r'-='
t_ATRIBUIMULT 	= r'\*='
t_ATRIBUIDIV    = r'/='
t_MOD           = r'%='

t_MAIS          = r'\+'
t_MENOS			= r'-'
t_MULTIPLICACAO	= r'\*'
t_DIVIDE        = r'/'
t_ATRIBUICAO    = r'='



#t_ASPAS			= r'\"'
@TOKEN(r'[a-zA-Z_][a-zA-Z_0-9]*')
def t_NOME(t):
    if t.value in reservados:# VERIFICANDO SE A PALAVRA É RESERVADA
        t.type = reservados[ t.value ]
    return t


c1 = 0
linha_aux = 0
@TOKEN(r'/\*(.*)')
def t_COMENTARIO_ABRINDO(t):
    global c1,linha_aux
    c1 += 1
    linha_aux = t.lineno 
    print(f'\033[0;30;42mABRINDO\033[m {t.value}')
    if '*/' not in t.value:
        print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mCOMENTÁRIO NÃO TERMINA\033[m, LINHA: {t.lineno}')
    pass


c2 = 0
@TOKEN(r'\*/')
def t_COMENTARIO_FECHANDO(t):
    global c2
    c2 += 1
    print(f'\033[0;30;42mFECHOU\033[m {t.value}')


@TOKEN(r'(/\*(.|\n)*?\*/)|(/\*.*)')
def t_COMENTARIO_MESMA_LINHA(t):
    if t.value.find('*/') == -1:
        print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mCOMENTÁRIO NÃO TERMINA\033[m, LINHA: {t.lineno}')
    pass


@TOKEN(r'\d+') #DECORETOR
def t_NUMERO(t):
    t.value = int(t.value)
    return t


# Define uma regra para que possamos rastrear números de linha
@TOKEN(r'\n+')
def t_newline(t):
    t.lexer.lineno += len(t.value)


# Regra de tratamento de erros - quando caracteres ilegais são detectados
def t_error(t):
    print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mCARACTER INVÁLIDO\033[m -{t.value[0]} LINHA = {t.lineno}') 
    t.lexer.skip(1)

    
# isso produz vários tipos de informações de depuração, incluindo todas as regras e as expressoes regulares
#simboliza a leitura de entrada da entrada padrão ou de um arquivo especificado na linha do comando
lexer = lex.lex()

arquivo = open('entrada1.txt', 'r')
arq = arquivo.read()
lexer.input(arq)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(f'TIPO = {tok.type}, VALOR = {tok.value}, LINHA = {tok.lineno}')
if c1 > c2:
    print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mCADEIA DE CARACTERES OCUPA MAIS DE UMA LINHA\033[m, LINHA = {linha_aux}')

arquivo.close()


