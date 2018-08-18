
import sys
import ply.yacc as yacc
# from Mparser import Mparser
from TreePrinter import TreePrinter
import logging

sys.path.insert(0, '../lab-2-parser')

import my_parser

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example0.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = yacc.yacc(module=my_parser)
    text = file.read()
    ast = parser.parse(text, lexer=my_parser.scanner.lexer)
    ast.printTree()