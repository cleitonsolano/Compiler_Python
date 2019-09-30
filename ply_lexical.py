import sys
from ply import *
from ply.lex import TOKEN

'''
PALAVRAS RESERVADAS
'''

reservados = {
    'programa'  : 'PROGRAMA',
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
          'MENORIGUAL', 'MAIORIGUAL','NORMALSTRING',
          'MOD','ASPASD') + tuple(reservados.values()) 

'''
TOKENS E SIMBULOS
( ) [ ] { } , ; + - * / == != > >= < <= || && ! = += -= *= /= %= ? :
'''

t_ignore        = ' \t'


t_EPAREN        = r'\('
t_DPAREN        = r'\)'
t_ECOCHETE      = r'\]'
t_DCOCHETE      = r'\['
t_ECHAVES       = r'\{'
t_DCHAVES       = r'\}'


t_VIRGULA      = r','
t_PVIRGULA      = r';'
t_OU 			= r'\|\|'
t_E             = r'&&'
t_EXCLAMACAO    = r'!'
t_INTERROGACAO  = r'\?'
t_DOISP         = r':'


t_ATRIBUICAO    = r'=='
t_DIFERENTE		= r'!='
t_MENOR			= r'<'
t_MAIOR			= r'>'
t_MENORIGUAL    = r'<='
t_MAIORIGUAL    = r'>='


t_MAIS          = r'\+'
t_MENOS			= r'-'
t_MULTIPLICACAO	= r'\*'
t_DIVIDE        = r'/'
t_IGUAL         = r'='

t_ASPASD = '\"'



@TOKEN(r'[a-zA-Z_][a-zA-Z_0-9]*')
def t_NOME(t):
    if t.value in reservados:# VERIFICANDO SE A PALAVRA É RESERVADA
        t.type = reservados[ t.value ]
    return t

'''# TESTE PARA LOCALIZAR O ABRE E FECHA COMENTÁRIO
@TOKEN(r'/\*(.*)')
def t_COMENTARIO_ABRINDO(t): 
    print(f'\033[0;30;42mABRINDO\033[m {t.value}')


@TOKEN(r'\*/')
def t_COMENTARIO_FECHANDO(t):
    print(f'\033[0;30;42mFECHOU\033[m {t.value}')
'''

@TOKEN(r'(/\*(.|\n)*?\*/)|(/\*.*)')
def t_COMENTARIO_MESMA_LINHA(t):
    #if t.value.find('*/') == -1:
    if '*/' not in t.value:
        print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mCOMENTÁRIO NÃO TERMINA\033[m, LINHA: {t.lineno}')
    elif '\n' in t.value:
        print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mCOMENTÁRIO OCUPA MAIS DE UMA LINHA\033[m, LINHA: {t.lineno}')
   # pass


@TOKEN(r'\d+') #DECORETOR
def t_NUMERO(t):
    t.value = int(t.value)
    return t


#pega qualquer cadeia dentro de ""
def t_NORMALSTRING(t):
    r'\"([^\\\n]|(\\.))*?\"'

    return t


# Define uma regra para que possamos rastrear números de linha
@TOKEN(r'\n+')
def t_newline(t):
    t.lexer.lineno += len(t.value)


# Regra de tratamento de erros - quando caracteres ilegais são detectados
def t_error(t):
    print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mCARACTER INVÁLIDO\033[m -{t.value[0]} LINHA = {t.lineno}') 
    t.lexer.skip(1)
    raise SystemExit


# isso produz vários tipos de informações de depuração, incluindo todas as regras e as expressoes regulares
#simboliza a leitura de entrada da entrada padrão ou de um arquivo especificado na linha do comando

'''
scanner = lex.lex()

arquivo = open('entrada1.txt', 'r')
arq = arquivo.read()
sacanner.input(arq)
while True:
    tk = scanner.token()
    if not tk:
        break
    print(f'TIPO = {tk.type}, VALOR = {tk.value}, LINHA = {tk.lineno}')
arquivo.close()
'''


if __name__ == '__main__':
     lex.runmain()


lexer = lex.lex()

