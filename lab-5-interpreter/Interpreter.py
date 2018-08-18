
import sys

sys.path.insert(0, '../lab-2-parser')
sys.path.insert(0, '../lab-3-syntax-tree')
sys.path.insert(0, '../lab-4-semantic-analysis')

import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *


sys.setrecursionlimit(10000)

class Interpreter(object):
    def __init__(self, out = None):
        print("interpreter init")
        self.memoryStack = MemoryStack()
        pass

    @on('node')
    def visit(self, node):
        print("node interpreted")
        pass

    @when(AST.Program)
    def visit(self, node):
        print("program interpreted")
        for instruction in node.instructions:
            print("\n new instruction")
            print("type: " + str(instruction.type))
            instruction.accept(self)



    @when(AST.If)
    def visit(self, node):
        print("if")
        condition = node.condition.accept(self)
        if condition:
            self.memoryStack.pushMemory(Memory("IF_STATEMENT"))
            node.then_instruction.accept(self)
            self.memoryStack.popMemory()

    @when(AST.Comparision)
    def visit(self, node):
        print("comparision")
        operation = node.op 
        left = node.left
        right = node.right

        if left.type == "VARIABLE":
            left = self.memoryStack.getVariableValue(left.name)
            print(left)



    @when(AST.Assignment)
    def visit(self, node):
        value = node.value.accept(self) 
        

