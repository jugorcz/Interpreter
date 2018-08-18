# Defintion of node classes for Abstract Syntax Tree

class AST(object):
    def __init__(self, line):
        self.line = line
    
    def accept(self, visitor):
        return visitor.visit(self)

# it is OK
class Program(AST):
    def __init__(self, instructions, line):
        self.type = "PROGRAM"
        self.instructions = instructions
        self.line = line

# it is OK
class Assignment(AST):
    def __init__(self, ref, op, value, line):
        self.ref = ref
        self.type = self.op = op
        self.value = value
        self.line = line

# it is OK
class Refference(AST):
    def __init__(self, id, vector, line):
        self.type = "REF"
        self.id = id
        self.indices = vector
        self.line = line

# it is OK
class If(AST):
    def __init__(self, op, condition, then_instruction):
        self.type = self.op = op
        self.condition = condition
        self.then_instruction = then_instruction

# OK
class IfElse(AST):
    def __init__(self, if_op, condition, then_instruction, else_op, else_instruction):
        self.type = if_op + "_" + else_op
        self.if_op = if_op
        self.condition = condition
        self.then_instruction = then_instruction
        self.else_op = else_op
        self.else_instruction = else_instruction  

# OK
class For(AST):
    def __init__(self, op, iterator, instruction):
        self.type = self.op = op
        self.iterator = iterator
        self.instruction = instruction    

# OK
class While(AST):
    def __init__(self, op, condition, instruction):
        self.type = self.op = op   
        self.condition = condition
        self.instruction = instruction

# OK
class Command(AST):
    def __init__(self, command, line):
        self.type = self.command = command
        self.line = line

# OK
class Return(AST):
    def __init__(self, command, line, arg=None):
        self.type = self.command = command
        self.arg = arg
        self.line = line

# OK
class Print(AST):
    def __init__(self, command, arg, line):
        self.type = self.command = command
        self.arg = arg
        self.line = line

# OK
class Compound(AST):
     def __init__(self, code=None):
        self.type = "BLOCK OF CODE"
        self.code = code

# BinOp is OK
class BinOp(AST):
    def __init__(self, left, op, right, line):
        self.left = left
        self.type = self.op = op
        self.right = right
        self.line = line

# DotBinOp is OK
class DotBinOp(AST):
    def __init__(self, left, op, right, line):
        self.left = left
        self.type = self.op = op
        self.right = right
        self.line = line

# OK
class Uminus(AST):
    def __init__(self, expression):
        self.type = "UMINUS"
        self.expr = expression

# OK
class Transposition(AST):
    def __init__(self, matrix, line):
        self.type = "TRANSPOSE"
        self.matrix = matrix
        self.line = line
        
# OK
class Comparision(AST):
     def __init__(self, left, op, right, line):
        self.left = left
        self.type = self.op = op
        self.right = right
        self.line = line

# OK Special is ZEROS/ONES/EYE
class SpecialMatrix(AST):
    def __init__(self, op, value, line):
        self.type = self.op = op
        self.value = value
        self.line = line
        self.elem_type = Integer(None, line)

# OK
class Iterator(AST):
    def __init__(self, name, start, stop, line):
        self.type = "RANGE"
        self.name = name
        self.start = start
        self.stop = stop
        self.line = line

# OK
class Matrix(AST):
    def __init__(self,line):
        self.type = "MATRIX"
        self.vectors = []
        self.line = line
        self.rows = None
        self.columns = None
        self.elem_type = Integer(None, line)

# it is OK
class Vector(AST):
    def __init__(self,line):
        self.type = "VECTOR"
        self.elements = []
        self.line = line
        self.size = None

# it is OK
class Integer(AST):
    def __init__(self, value, line):
        self.type = "INTEGER"
        self.value = value
        self.line = line

# it is OK
class Float(AST):
    def __init__(self, value, line):
        self.type = "FLOAT"
        self.value = value
        self.line = line
      
# Variable is OK
class Variable(AST):
    def __init__(self, name, line):
        self.type = "VARIABLE"
        self.name = name
        self.line = line

# OK
class Error(AST):
    def __init__(self, message):
        self.type = "error"
        self.message = message
        