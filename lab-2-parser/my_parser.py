#!/usr/bin/python
import sys
import ply.yacc as yacc

sys.path.insert(0, '../lab-1-scanner')
import scanner

sys.path.insert(0, '../lab-3-syntax-tree')
from AST import *

scanner = scanner
tokens = scanner.tokens

precedence = (
   ("nonassoc", "IFX"),
   ("nonassoc", "ELSE"),
   ("nonassoc", 'LESS_THAN', 'GREATER_THAN', 'LESS_OR_EQUAL_THAN', 'GREATER_OR_EQUAL_THAN', 'NOT_EQUAL', 'EQUAL'),
   ("left", 'PLUS', 'MINUS', 'DOTADD', 'DOTSUB'),
   ("left", 'TIMES', 'DIVIDE', 'DOTMUL', 'DOTDIV'),
   ("right", '='),
   ("right", 'ADDASSIGN', 'SUBASSIGN'),
   ("right", 'MULASSIGN', 'DIVASSIGN'),
   ("right", 'APOSTROPHE'),
   ("right", 'UMINUS'))

# OK
def p_program(p):
    """program : instructions"""
    p[0] = Program(p[1], p.lineno(1))


# OK
def p_instructions(p):
    """instructions : instruction
                    | instruction instructions"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

# OK
def p_instruction(p):
    """instruction : assignment
                   | ifx
                   | if_else
                   | for
                   | while
                   | command
                   | return
                   | print
                   | compound"""
    p[0] = p[1]

# OK
def p_assignment(p):
    """assignment : ID '=' expression ';'
                  | ID ADDASSIGN expression ';'
                  | ID SUBASSIGN expression ';'
                  | ID MULASSIGN expression ';'
                  | ID DIVASSIGN expression ';'
                  | ID '[' vector ']' '=' expression ';'"""
    if len(p) == 5: 
      p[0] = Assignment(Variable(p[1],p.lineno(1)), p[2], p[3], p.lineno(1))
    else: 
      p[0] = Assignment(
                        ref = Refference(
                                          id = Variable(
                                                          name = p[1],
                                                          line = p.lineno(1)
                                                          ), 
                                          vector = p[3],
                                          line = p.lineno(1)
                                        ), 
                        op = p[5], 
                        value = p[6], 
                        line = p.lineno(1))

# OK ??
def p_assignment_refference(p):
    """assignment : ID '=' ID '[' vector ']' ';'"""
    p[0] = Assignment(
                      ref = Variable(
                                p[1], 
                                p.lineno(1)
                              ), 
                      op = p[2], 
                      value = Refference(
                                          id = Variable(
                                                          p[3],
                                                          p.lineno(1)
                                          ), 
                                          vector = p[5],
                                          line = p.lineno(1)
                                ),
                      line = p.lineno(1)
                      )

# OK
def p_ifx(p):
  """ifx : IF '(' condition ')' instruction %prec IFX"""
  p[0] = If(p[1], p[3], p[5])

# OK
def p_if_else(p):
    """if_else : IF '(' condition ')' instruction ELSE instruction"""
    p[0] = IfElse(p[1], p[3], p[5], p[6], p[7])

# OK
def p_for(p):
    """for : FOR iterator instruction"""
    p[0] = For(p[1], p[2], p[3])

# OK
def p_iterator(p):
    """iterator : ID '=' factor ':' factor """
    p[0] = Iterator(Variable(p[1],p.lineno(1)), p[3], p[5], p.lineno(1))

# OK
def p_while(p):
    """while : WHILE '(' condition ')' instruction"""
    p[0] = While(p[1], p[3], p[5])

# OK
def p_command(p):
    """command : BREAK ';'
               | CONTINUE ';'"""
    p[0] = Command(p[1], p.lineno(1))

# OK
def p_return(p):
    """return : RETURN ';' """
    p[0] = Return(p[1], p.lineno(1))

# OK
def p_return_expression(p):
    """return : RETURN expression ';' """
    p[0] = Return(p[1], p.lineno(1), p[2])

# OK
def p_print(p):
    """print : PRINT DOUBLEAPOSTROPHE expression DOUBLEAPOSTROPHE ';'
             | PRINT vector ';' """
    if len(p) == 4: 
      p[0] = Print(p[1], p[2], p.lineno(1))
    else: p[0] = Print(p[1], p[3], p.lineno(1))

# OK
def p_compound(p):
    """compound : '{' program '}' 
                | '{' '}'  """
    if len(p) == 3:  p[0] = Compound()
    else: p[0] = Compound(p[2])

# OK
def p_condition(p):
    """condition : expression_comparison"""
    p[0] = p[1]

# OK
def p_variable_factor(p):
    """factor : ID"""
    p[0] = Variable(p[1],p.lineno(1))

# OK
def p_numerical_factor(p):
    """factor : number"""
    p[0] = p[1]

# OK
def p_int_number(p):
    """number : INTNUM"""
    p[0] = Integer(p[1], p.lineno(1))

# OK
def p_float_number(p):
    """number : FLOATNUM"""
    p[0] = Float(p[1], p.lineno(1))

# OK
def p_expression(p):
    """expression : factor
                  | expression_bin_op
                  | expression_dot_bin_op
                  | expression_uminus
                  | expression_transposition
                  | expression_comparison
                  | expression_matrix
                  | expression_table"""
    p[0] = p[1]

# OK
def p_expression_bin_op(p):
    """expression_bin_op : expression PLUS expression
                         | expression MINUS expression
                         | expression TIMES expression
                         | expression DIVIDE expression"""
    p[0] = BinOp(p[1], p[2], p[3], p.lineno(1))

# OK
def p_expression_dot_bin_op(p):
    """expression_dot_bin_op : expression DOTADD expression
                             | expression DOTSUB expression
                             | expression DOTMUL expression
                             | expression DOTDIV expression"""
    p[0] = DotBinOp(p[1], p[2], p[3], p.lineno(1))

# ok
def p_expression_uminus(p):
    """expression_uminus : MINUS expression %prec UMINUS"""
    p[0] = Uminus(p[2])

# OK -> expression changed for ID (ID macierzy)
def p_expression_transposition(p):
    """expression_transposition : ID APOSTROPHE"""
    p[0] = Transposition(Variable(p[1], p.lineno(1)), line = p.lineno(1))

# OK
def p_expression_comparison(p):
    """expression_comparison : expression LESS_THAN expression
                             | expression GREATER_THAN expression
                             | expression LESS_OR_EQUAL_THAN expression
                             | expression GREATER_OR_EQUAL_THAN expression
                             | expression NOT_EQUAL expression
                             | expression EQUAL expression"""
    p[0] = Comparision(p[1], p[2], p[3], p.lineno(1))

# OK
def p_expression_matrix(p):
    """expression_matrix : ZEROS '(' factor ')'
                         | EYE '(' factor ')'
                         | ONES '(' factor ')' """
    p[0] = SpecialMatrix(p[1], p[3], p.lineno(1))

# OK
def p_empty_list(p):
    """expression_table : '[' ']' """
    p[0] = Vector(p.lineno(1))
    #nothing will be append

# OK
def p_non_empty_matrix(p):
    """expression_table : '[' matrix ']' """
    #matrix = Matrix(p.lineno(1))
    #matrix.vectors.append(p[2])
    p[0] = p[2]

# OK
def p_matrix(p):
    """matrix : vector ';' matrix
              | vector """
    if len(p) == 2:
     p[0] = Matrix(p.lineno(1))
     p[0].vectors.append(p[1])
    else: 
      p[3].vectors.append(p[1])
      p[0] = p[3]

# OK
def p_vector(p):
    """vector : factor ',' vector
              | factor """
    if len(p) == 2:
      p[0] = Vector(p.lineno(1))
      p[0].elements.append(p[1])
    else: 
      p[3].elements.append(p[1])
      p[0] = p[3]


# TODO ??
def p_error(p):
    if p:
      print("{0} Parser: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
        #error = Error("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
        #error.printTree()
    else:
        error = Error("Unexpected end of input")
        #error.printTree()


parser = yacc.yacc()
