from __future__ import print_function
import AST


indent_print = "|    "

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @addToClass(AST.AST)
    def printTree(self, indent=0):
        print(self.type)


    @addToClass(AST.Program)
    def printTree(self, indent=0):
        for instruction in self.instructions:
            instruction.printTree(indent)


    @addToClass(AST.Assignment)
    def printTree(self, indent=0):
        print(indent_print * indent + self.type)
        self.ref.printTree(indent + 1)
        self.value.printTree(indent + 1)


    @addToClass(AST.Refference)
    def printTree(self, indent=0):
        print(indent_print * indent + self.type)
        self.id.printTree(indent + 1)
        self.vector.printTree(indent + 1)


    @addToClass(AST.If)
    def printTree(self, indent=0):
        print(indent_print * indent + self.type)
        self.condition.printTree(indent + 1)
        self.then_instruction.printTree(indent + 1)

    
    @addToClass(AST.IfElse)
    def printTree(self, indent=0):
        print(indent_print * indent + self.if_op)
        self.condition.printTree(indent + 1)
        self.then_instruction.printTree(indent + 1)
        print(indent_print * indent + self.else_op)
        self.else_instruction.printTree(indent + 1)


    @addToClass(AST.For)
    def printTree(self, indent=0):
        print(indent_print * indent + self.type)
        self.iterator.printTree(indent + 1)
        self.instruction.printTree(indent + 1)


    @addToClass(AST.While)
    def printTree(self, indent=0):
        print(indent_print * indent + self.type)
        self.condition.printTree(indent + 1)
        self.instruction.printTree(indent + 1)


    @addToClass(AST.Command)
    def printTree(self, indent=0):
        print(indent_print * indent + self.type)


    @addToClass(AST.Return)
    def printTree(self, indent=0):
        print(indent_print * indent + self.type)
        self.arg.printTree(indent + 1)


    @addToClass(AST.Print)
    def printTree(self, indent=0):
        print(indent_print * indent + self.type)
        if self.arg != None:
            self.arg.printTree(indent + 1)
    

    @addToClass(AST.Compound)
    def printTree(self, indent=0):
        if self.code != None:
            self.code.printTree(indent)


    @addToClass(AST.BinOp)
    def printTree(self, indent=0):
        print(indent_print * indent + self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)


    @addToClass(AST.DotBinOp)
    def printTree(self, indent=0):
        print(indent_print * indent + self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)


    @addToClass(AST.Uminus)
    def printTree(self, indent=0):
        print(indent_print * indent + self.type)
        self.expr.printTree(indent + 1)


    @addToClass(AST.Transposition)
    def printTree(self, indent=0):
        print(indent_print * indent + self.type)
        self.matrix.printTree(indent + 1)


    @addToClass(AST.Comparision)
    def printTree(self, indent=0):
        print(indent_print * indent + self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)


    @addToClass(AST.SpecialMatrix)
    def printTree(self, indent=0):
        print(indent_print * indent + self.op)
        self.value.printTree(indent + 1)


    @addToClass(AST.Iterator)
    def printTree(self, indent=0):
        self.name.printTree(indent)
        print(indent_print * indent + self.type)
        self.start.printTree(indent + 1)
        self.stop.printTree(indent + 1)


    @addToClass(AST.Matrix)
    def printTree(self, indent=0):
        print(indent_print * indent + self.type)
        for vector in self.vectors:
            vector.printTree(indent + 1)


    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print(indent_print * indent + self.type)
        for element in self.elements:
            element.printTree(indent + 1)


    @addToClass(AST.Integer)
    def printTree(self, indent=0):
        print(indent_print * indent + str(self.value))


    @addToClass(AST.Float)
    def printTree(self, indent=0):
        print(indent_print * indent + str(self.value))


    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print(indent_print * indent + str(self.name))


    @addToClass(AST.Error)
    def printTree(self, indent=0):
        print("Error: " + self.message)

