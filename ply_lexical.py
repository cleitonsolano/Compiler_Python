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
    'execute'   : 'EXECUTE',
    'e'         :   'E',
    'ou'        :   'OU'
}   

tokens = ('NOME', 'INTEIRO', 'MAIS', 'MENOS', 'MULTIPLICACAO', 'DIVIDE', 'ATRIBUICAO',
          'EPAREN', 'DPAREN', 'ECOCHETE', 'DCOCHETE', 'ECHAVES', 'DCHAVES', 'VIRGULA', 'PVIRGULA',
          'EXCLAMACAO', 'INTERROGACAO', 'DOISP', 'IGUAL', 'DIFERENTE', 'MENOR', 'MAIOR',
          'MENORIGUAL', 'MAIORIGUAL','NORMALSTRING',
          'MOD','ASPASD', 'CCONSTANTE') + tuple(reservados.values()) 

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
t_EXCLAMACAO    = r'!'
t_INTERROGACAO  = r'\?'
t_DOISP         = r':'


t_ATRIBUICAO    = r'=='
t_DIFERENTE     = r'!='
t_MENOR         = r'<'
t_MAIOR         = r'>'
t_MENORIGUAL    = r'<='
t_MAIORIGUAL    = r'>='


t_MAIS          = r'\+'
t_MENOS         = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVIDE        = r'/'
t_IGUAL         = r'='
t_MOD           = r'\%'

t_ASPASD = '\"'


def t_PROGRAMA(t):
    r'programa'
    return t

def t_CAR(t):
    r'car'
    return t

def t_INT(t):
    r'int'
    return t

def t_RETORNE(t):
    r'retorne'
    return t

def t_LEIA(t):
    r'leia'
    return t

def t_ESCREVA(t):
    r'escreva'
    return t

def t_NOVALINHA(t):
    r'novalinha'
    return t

def t_SE(t):
    r'se'
    return t

def t_ENTAO(t):
    r'entao'
    return t

def  t_SENAO(t):
    r'senao'
    return t

def t_ENQUANTO(t):
    r'entao'
    return t


@TOKEN(r'execute')
def t_EXECUTE(t):

    return t

@TOKEN(r'[a-zA-Z_][a-zA-Z_0-9]*')
def t_NOME(t):
    
    if t.value in reservados:# VERIFICANDO SE A PALAVRA É RESERVADA
        t.type = reservados[ str(t.value) ]
    
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
    raise SystemExit
   # pass


@TOKEN(r'\d+') #DECORETOR
def t_INTEIRO(t):
    t.value = int(t.value)
    return t


#pega qualquer cadeia dentro de ""
def t_NORMALSTRING(t):
    r'\"[^\"]*\"'

    t.value = t.value[1:-1]
    if t.value.find('\n') != -1:
        print(f'\033[0;30;41mERRO\033[m : \033[0;30;41mCADEIA DE CARACTERES OCUPA MAIS DE UMA LINHA\033[m, LINHA: {t.lineno}')
        raise SystemExit


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

def t_CCONSTANTE(t):
    r"\'.\'"
    t.value = t.value[1:-1]
    return t


# isso produz vários tipos de informações de depuração, incluindo todas as regras e as expressoes regulares
#simboliza a leitura de entrada da entrada padrão ou de um arquivo especificado na linha do comando


scanner = lex.lex()
arquivo = open('entrada1.txt', 'r')
arq = arquivo.read()
arquivo.close()
print("kkkkk")
scanner.input(arq)
print("kkkkk")
while True:
    print("kkkkk")
    tk = scanner.token()
    print("kkkkk")
    if not tk:
        break
    print(f'TIPO = {tk.type}, VALOR = {tk.value}, LINHA = {tk.lineno}')

'''
prin = lex.lex()
prin.input(open("entrada1.txt", "r").read())
while True:
    tok = prin.token()
    if not tok:
        break
        print(tok)
'''


if __name__ == '__main__':
     lex.runmain()


lexer = lex.lex()