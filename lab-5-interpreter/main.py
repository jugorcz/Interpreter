
import sys
import ply.yacc as yacc

sys.path.insert(0, '../lab-2-parser')
sys.path.insert(0, '../lab-3-syntax-tree')
sys.path.insert(0, '../lab-4-semantic-analysis')

import my_parser
import TreePrinter
import TypeChecker
import Interpreter


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)


    parser = yacc.yacc(module=my_parser)
    text = file.read()
    ast = parser.parse(text, lexer=my_parser.scanner.lexer)
    ast.printTree()

    # Below code shows how to use visitor
    
    typeChecker = TypeChecker.TypeChecker()
    typeChecker.visit(ast)

    ast.accept(Interpreter.Interpreter())
    # in future
    # ast.accept(OptimizationPass1())
    # ast.accept(OptimizationPass2())
    # ast.accept(CodeGenerator())
    