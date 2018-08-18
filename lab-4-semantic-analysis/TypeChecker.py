#!/usr/bin/python
import sys

sys.path.insert(0, '../lab-3-syntax-tree')
import AST
import SymbolTable

from SymbolTable import VariableSymbol

from collections import defaultdict

class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)


    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.AST):
                            self.visit(item)
                elif isinstance(child, AST.AST):
                    self.visit(child)


types = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

# rules for BinOp
for op in ('+', '-', '*', '/'):
    types[op]['INTEGER']['INTEGER'] = 'INTEGER'
    types[op]['FLOAT']['FLOAT'] = 'FLOAT'
    types[op]['FLOAT']['INTEGER'] = 'FLOAT'
    types[op]['INTEGER']['FLOAT'] = 'FLOAT'

# rules for Comparision
for op in ('<', '>', '==', '!=', '<=', '>='):
    types[op]['INTEGER']['INTEGER'] = 'INTEGER'
    types[op]['FLOAT']['FLOAT'] = 'INTEGER'
    types[op]['FLOAT']['INTEGER'] = 'INTEGER'
    types[op]['INTEGER']['FLOAT'] = 'INTEGER'

# rules for Assignment
for op in ('=', '+=', '-=', '/='):
    types[op]['INTEGER']['INTEGER'] = 'INTEGER'
    types[op]['FLOAT']['FLOAT'] = 'FLOAT'
    types[op]['FLOAT']['INTEGER'] = 'FLOAT'
    types[op]['INTEGER']['FLOAT'] = 'INTEGER'
    types[op]['MATRIX']['MATRIX'] = 'MATRIX'


class TypeChecker(NodeVisitor):

    def __init__(self):
        self.symtable = SymbolTable.SymbolTable(parent = None, name = 'root')


    def visit_Program(self, node):
        print("wisit program")
        for instruction in node.instructions:
            self.visit(instruction)
    

    # OK
    def visit_Assignment(self, node):
        print("wisit assignment")
        r_node = self.visit(node.value)
        op = node.op
        
        if r_node is not None:
            r_type = r_node.type
            name = node.ref.name
            if op == "=":
                self.symtable.put(name, VariableSymbol(name, r_type, r_node))
            else:
                if self.visit(node.ref) is not None:
                    l_node = self.visit(node.ref)
                    l_type = l_node.type
                    new_type = types[op][l_type][r_type]
                    if new_type is None:
                        print("Line {}: Assignment on different types: '{}' and '{}'".format(node.line, l_type, r_type))
                        return
                    self.symtable.put(name, VariableSymbol(name, new_type, r_node))

    # OK
    def visit_Refference(self, node):
        # sprawdzam czy taka macierz istnieje
        matrix_variable = self.visit(node.id)
        if matrix_variable is None:
            return None
        elif matrix_variable.type != "MATRIX":
            print("Line {}: Reffernece to variable of type '{}'".format(node.line, matrix_variable.type))
            return None

        # sprawdzam czy podano wspolrzedne
        coordinates = self.visit(node.indices)
        if len(coordinates) != 2:
            print('Line {}: Matrix are only two dimensional, indices of {} dimensions were provided'.format(node.line, len(coordinates)))
            return None

        for coord in coordinates:  
            if coord.type != 'INTEGER':
                print('Line {}: Matrix coordinates should be of type integer'.format(node.line))
                return None
         
        try:
            # sprawdzenie zakresu
            col = self.visit(coordinates[0])
            row = self.visit(coordinates[1])

            if row.value < 0 or row.value >= matrix_variable.rows:
                print("Line {}: Row out of range, should be less than {}, is {}".format(node.line, matrix_variable.rows, row.value))
                return None

            if col.value < 0 or col.value >= matrix_variable.columns:
                print("Line {}: Column out of range, should be less than {}, is {}".format(node.line, matrix_variable.columns, col.value))
                return None

            try:
                return matrix_variable.vectors[row].elements[col]
            except:
                return matrix_variable.elem_type
        except:
            return None

    # OK
    def visit_If(self, node):
        self.visit(node.condition)
        self.symtable = self.symtable.pushScope("if")
        self.visit(node.then_instruction)
        self.symtable = self.symtable.popScope()
    
    # OK
    def visit_IfElse(self, node):
        self.visit(node.condition)
        self.symtable = self.symtable.pushScope("if_else")
        self.visit(node.then_instruction)
        self.symtable = self.symtable.popScope()
        self.symtable = self.symtable.pushScope("else")
        self.visit(node.else_instruction)
        self.symtable = self.symtable.popScope()

    # OK
    def visit_For(self, node):
        self.symtable = self.symtable.pushScope("loop")
        self.visit(node.iterator)
        self.visit(node.instruction)
        self.symtable = self.symtable.popScope()

    # OK
    def visit_While(self, node):
        self.visit(node.condition)
        self.symtable = self.symtable.pushScope("loop")
        self.visit(node.instruction)
        self.symtable = self.symtable.popScope()

    # OK
    # BREAK and CONTINUE
    def visit_Command(self, node):
        if self.symtable.get('loop') == 0 or self.symtable.get('loop') is None:
            print("Line {}: Command '{}' outside the loop".format(node.line, node.command))
  

    # OK
    def visit_Return(self, node):
        if node.arg is not None:
            self.visit(node.arg)
        if self.symtable.get('function') == 0 or self.symtable.get('function') is None:
            print("Line {}: Command '{}' outside the function".format(node.line, node.command))
  

    # OK
    def visit_Print(self, node):
        self.visit(node.arg)


    # OK
    def visit_Compound(self, node):
        if node.code is not None:
            self.visit(node.code)


    # OK
    def visit_BinOp(self, node):
        node_1 = self.visit(node.left)
        type_1 = node_1.type
        node_2 = self.visit(node.right)
        type_2 = node_2.type
        op = node.op
        result_type = types[op][type_1][type_2]
        if result_type is None:
            print("Line {}: Unsupoorted operation '{}' on types '{}' and '{}'".format(node_2.line, op, type_1, type_2))
        else:
            node_1.type = result_type
            return node_1

    # OK
    def visit_DotBinOp(self, node):
        node_1 = self.visit(node.left)
        type_1 = node_1.type
        node_2 = self.visit(node.right)
        type_2 = node_2.type
        op = node.op
        line = node.left.line
        if type_1 != "MATRIX":
            print("Line {}: Unsupoorted operation '{}' on types '{}' and '{}'".format(line, op, type_1, type_2))
            return None
        if type_2 != "MATRIX":
            print("Line {}: Unsupoorted operation '{}' on types '{}' and '{}'".format(line, op, type_1, type_2))
            return None

        if op in [".+", ".-"]:
            if node_1.rows != node_2.rows or node_1.columns != node_2.columns:
                print("Line {}: Unsupoorted operation '{}' on matrix of sizes {} and {}".format(line, op, (node_1.rows, node_1.columns),  (node_2.rows, node_2.columns)))
                return None
        
        if op in [".*", ".-/"]:
            if node_1.rows != node_2.columns or node_2.rows != node_1.columns:
                print("Line {}: Unsupoorted operation '{}' on matrix of sizes {} and {}".format(line, op, (node_1.rows, node_1.columns),  (node_2.rows, node_2.columns)))
                return None
            else:
                node_1.columns = node_2.columns
        return node_1

    # ?OK
    def visit_Uminus(self, node):
        return self.visit(node.expr)

    # OK
    def visit_Transposition(self, node):
        visited_node = self.visit(node.matrix)
        visited_type = visited_node.type
        if visited_type != "MATRIX":
            print("Line {}: Transponsition not possible on type '{}'".format(node.line, visited_type))
            return None
        else:
            visited_node.columns, visited_node.rows = visited_node.rows, visited_node.columns
            return visited_node

    # OK
    def visit_Comparision(self, node):
        node_1 = self.visit(node.left)
        type_1 = node_1.type
        node_2 = self.visit(node.right)
        type_2 = node_2.type
        op = node.op
        line = node.left.line
        result_type = types[op][type_1][type_2]
        if result_type is None:
            print("Line {}: Unsupoorted operation '{}' on types '{}' and '{}'".format(line, op, type_1, type_2))
        else:
            return AST.Integer(None, node.line)

    # OK
    def visit_SpecialMatrix(self, node):
        size_node = self.visit(node.value)
        if size_node is not None:
            size_type = size_node.type
            size_value = size_node.value
            if size_type == "INTEGER":
                matrix = AST.Matrix(node.line)
                matrix.columns = matrix.rows = size_value
                return matrix
            else:
                print('Line {}: Matrix size has to be of type integer'.format(node.line))
                return None
        else:
            return None

    # OK
    def visit_Iterator(self, node):
        variable = node.name
        start_node = self.visit(node.start)
        start_type = start_node.type
        stop_node = self.visit(node.stop)
        stop_type = stop_node.type
        if start_type != 'INTEGER' or stop_type != 'INTEGER':
            print("Line {}: Range should be defined by integers".format(node.line))
            return None
        else:
            self.symtable.put(variable.name, VariableSymbol(variable.name, start_type, start_node))

    # OK
    def visit_Matrix(self, node):
        visited_vectors = [self.visit(vector) for vector in node.vectors]
        rows = len(visited_vectors)
        first_vector_len = len(visited_vectors[0])

        for vector in visited_vectors:
            vector_len = len(vector)
            if first_vector_len != vector_len:
                print('Line {}: Rows have different length'.format(vector[0].line))
                return None

        node.columns = first_vector_len
        node.rows = len(visited_vectors)
        # node.line = node.vectors[0].elements[0].line
        return node
        
    # OK
    def visit_Vector(self, node): 
        return [self.visit(element) for element in node.elements]

    # OK
    def visit_Variable(self, node):
        variable = self.symtable.get(node.name)
        if variable is not None:
            return variable.node
        else:
            print("Line {}: Variable '{}' not defined".format(node.line, node.name))
            return None

    # OK
    def visit_Integer(self, node):
        return node

    # OK
    def visit_Float(self, node):
        return node

    # OK
    def visit_Error(self, node):
        return node