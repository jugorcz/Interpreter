import sys
import ply.lex as lex
import scanner


def main():
    #build the lex
    lexer = scanner.lexer

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    lexer.input(text) # Give the lexer some input

    # Tokenize
    for token in lexer:
        print("(%d): %s(%s)" % (token.lineno, token.type, token.value))
    #The tokens returned by lexer.token() are instances of LexToken. 
    #This object has attributes tok.type, tok.value, tok.lineno, and tok.lexpos.

if __name__ == '__main__':
    main()