import sys
import ply.lex as lex

#list of token names, this is always required
#all lexers must provide a list tokens that defines all od the possible token names
#that can be produced by the lexer
#token list is also used by the yacc.py module to identify terminals
tokens = (  
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'INTNUM', 'FLOATNUM', 'ID',
    'DOTADD', 'DOTSUB', 'DOTDIV', 'DOTMUL',
    'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
    'LESS_THAN', 'GREATER_THAN', 'LESS_OR_EQUAL_THAN', 'GREATER_OR_EQUAL_THAN',
    'NOT_EQUAL', 'EQUAL',
    'IF', 'ELSE', 'FOR', 'WHILE',
    'BREAK', 'CONTINUE', 'RETURN',
    'EYE', 'ZEROS', 'ONES',
    'PRINT',
    'DOUBLEAPOSTROPHE', 'APOSTROPHE')

#regular expression rules for simple tokens

t_EQUAL = r'=='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_OR_EQUAL_THAN = r'<='
t_GREATER_OR_EQUAL_THAN = r'>='
t_NOT_EQUAL = r'!='

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'

t_DOTADD = r'.\+'
t_DOTSUB = r'.-'
t_DOTMUL = r'.\*'
t_DOTDIV = r'./'

t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-=' 
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='

t_DOUBLEAPOSTROPHE = r'"'
t_APOSTROPHE =r'\''

literals = [ 
    '+', '-', '*', '/',             # binary operators
    '=',                            # assignment oparator
    '(' , ')', '[', ']', '{', '}',  # brackets
    ':',                            # range
    '\'',                           # transposition
    ',', ';'                        # other
    ]

#a string containing idnored characters (spaces and tabs)
t_ignore = '  \t'
t_ignore_COMMENT = r'(\#.*(?=\n))|(\#.*$)'

key_words = {
    'if': 'IF', 'else': 'ELSE', 'for': 'FOR', 'while': 'WHILE',
    'break': 'BREAK', 'continue': 'CONTINUE', 'return': 'RETURN',
    'eye': 'EYE', 'zeros': 'ZEROS', 'ones': 'ONES',
    'print': 'PRINT'
}

#regular expression rule with some action code

def t_FLOATNUM(t):
    #r'(\d+\.\d*)|(\d*\.\d+)'
    #r'\d+\.\d+'
    r'-?\d+\.\d*(e-?\d+)?'
    t.value = float(t.value)
    return t


def t_INTNUM(t):
    r'\d+'
    #r'-?\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = key_words.get(t.value, 'ID')
    return t


#define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


#error handling rule
def t_error(t) :
    print("Illegal character '%s' at line %d" % (t.value[0], t.lineno))
    t.lexer.skip(1)
    

#expose lexer
lexer = lex.lex()