import sys
import ply.yacc as yacc

sys.path.insert(0, '../lab-2-parser')
sys.path.insert(0, '../lab-3-syntax-tree')

import my_parser
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "init.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = yacc.yacc(module=my_parser)
    text = file.read()

    # building abstract syntax tree
    ast = parser.parse(text, lexer=my_parser.scanner.lexer)

    # using visitor
    typeChecker = TypeChecker()   
    typeChecker.visit(ast)
    