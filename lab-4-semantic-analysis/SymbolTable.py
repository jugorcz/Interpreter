#!/usr/bin/python
from symtable import Symbol

class VariableSymbol(Symbol):

    def __init__(self, name, type, node=None):
        self.name = name
        self.type = type
        self.node = node


class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        self.parent = parent
        self.name = name
        self.symbols = dict() # Return a new dictionary initialized from an optional positional argument and a possibly empty set of keyword arguments.


    def displaySymbols(self):
        print("Saved symbols: ")
        for a in iter(self.symbols):
            print(a)


    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        self.symbols[name] = symbol
        

    def get(self, name): # get variable symbol or fundef from <name> entry
        if name in self.symbols.keys():
            return self.symbols[name]
        elif self.parent is not None:
            return self.parent.get(name)
        else:
            return None


    def getParentScope(self):
        return self.parent


    def pushScope(self, name):
        # create new scope
        scope = SymbolTable(self, name)
        # counter up
        if name in self.symbols.keys():
            self.symbols[name] += 1
        else:
            self.symbols[name] = 1
        return scope


    def popScope(self):
        # get scope
        scope = self.getParentScope()
        # counter down
        scope.symbols[self.name] -= 1
        return scope


# w symbols licznik petli, jesli > 0 to znaczy ze return, break, cont OK, jesli nie to nie
# zmmiejszamy jesli push, zwiekszamy jesli pop
