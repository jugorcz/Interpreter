
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "nonassocIFXnonassocELSEnonassocLESS_THANGREATER_THANLESS_OR_EQUAL_THANGREATER_OR_EQUAL_THANNOT_EQUALEQUALleftPLUSMINUSDOTADDDOTSUBleftTIMESDIVIDEDOTMULDOTDIVright=rightADDASSIGNSUBASSIGNrightMULASSIGNDIVASSIGNrightAPOSTROPHErightUMINUSPLUS MINUS TIMES DIVIDE INTNUM FLOATNUM ID DOTADD DOTSUB DOTDIV DOTMUL ADDASSIGN SUBASSIGN MULASSIGN DIVASSIGN LESS_THAN GREATER_THAN LESS_OR_EQUAL_THAN GREATER_OR_EQUAL_THAN NOT_EQUAL EQUAL IF ELSE FOR WHILE BREAK CONTINUE RETURN EYE ZEROS ONES PRINT DOUBLEAPOSTROPHE APOSTROPHEprogram : instructionsinstructions : instruction\n                    | instruction instructionsinstruction : assignment\n                   | ifx\n                   | if_else\n                   | for\n                   | while\n                   | command\n                   | return\n                   | print\n                   | compoundassignment : ID '=' expression ';'\n                  | ID ADDASSIGN expression ';'\n                  | ID SUBASSIGN expression ';'\n                  | ID MULASSIGN expression ';'\n                  | ID DIVASSIGN expression ';'\n                  | ID '[' vector ']' '=' expression ';'assignment : ID '=' ID '[' vector ']' ';'ifx : IF '(' condition ')' instruction %prec IFXif_else : IF '(' condition ')' instruction ELSE instructionfor : FOR iterator instructioniterator : ID '=' factor ':' factor while : WHILE '(' condition ')' instructioncommand : BREAK ';'\n               | CONTINUE ';'return : RETURN ';' return : RETURN expression ';' print : PRINT DOUBLEAPOSTROPHE expression DOUBLEAPOSTROPHE ';'\n             | PRINT vector ';' compound : '{' program '}' \n                | '{' '}'  condition : expression_comparisonfactor : IDfactor : numbernumber : INTNUMnumber : FLOATNUMexpression : factor\n                  | expression_bin_op\n                  | expression_dot_bin_op\n                  | expression_uminus\n                  | expression_transposition\n                  | expression_comparison\n                  | expression_matrix\n                  | expression_tableexpression_bin_op : expression PLUS expression\n                         | expression MINUS expression\n                         | expression TIMES expression\n                         | expression DIVIDE expressionexpression_dot_bin_op : expression DOTADD expression\n                             | expression DOTSUB expression\n                             | expression DOTMUL expression\n                             | expression DOTDIV expressionexpression_uminus : MINUS expression %prec UMINUSexpression_transposition : ID APOSTROPHEexpression_comparison : expression LESS_THAN expression\n                             | expression GREATER_THAN expression\n                             | expression LESS_OR_EQUAL_THAN expression\n                             | expression GREATER_OR_EQUAL_THAN expression\n                             | expression NOT_EQUAL expression\n                             | expression EQUAL expressionexpression_matrix : ZEROS '(' factor ')'\n                         | EYE '(' factor ')'\n                         | ONES '(' factor ')' expression_table : '[' ']' expression_table : '[' matrix ']' matrix : vector ';' matrix\n              | vector vector : factor ',' vector\n              | factor "
    
_lr_action_items = {'ID':([0,3,4,5,6,7,8,9,10,11,12,15,19,20,21,23,24,25,26,27,28,29,30,32,33,34,35,46,47,51,52,53,54,57,59,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,91,92,97,98,99,100,101,102,103,104,105,107,109,128,132,133,134,135,140,143,144,145,146,147,],[13,13,-4,-5,-6,-7,-8,-9,-10,-11,-12,31,45,57,13,60,45,45,45,45,57,45,13,45,-25,-26,-27,-35,45,57,-36,-37,45,-34,-32,-22,57,-28,45,45,45,45,45,45,45,45,45,45,45,45,45,45,57,57,57,-30,57,-31,57,-13,-14,-15,-16,-17,13,13,57,45,-20,57,-24,-29,13,-23,-19,-18,-21,]),'IF':([0,3,4,5,6,7,8,9,10,11,12,21,30,33,34,35,46,52,53,57,59,70,73,97,99,101,102,103,104,105,107,109,133,135,140,143,144,145,146,147,],[14,14,-4,-5,-6,-7,-8,-9,-10,-11,-12,14,14,-25,-26,-27,-35,-36,-37,-34,-32,-22,-28,-30,-31,-13,-14,-15,-16,-17,14,14,-20,-24,-29,14,-23,-19,-18,-21,]),'FOR':([0,3,4,5,6,7,8,9,10,11,12,21,30,33,34,35,46,52,53,57,59,70,73,97,99,101,102,103,104,105,107,109,133,135,140,143,144,145,146,147,],[15,15,-4,-5,-6,-7,-8,-9,-10,-11,-12,15,15,-25,-26,-27,-35,-36,-37,-34,-32,-22,-28,-30,-31,-13,-14,-15,-16,-17,15,15,-20,-24,-29,15,-23,-19,-18,-21,]),'WHILE':([0,3,4,5,6,7,8,9,10,11,12,21,30,33,34,35,46,52,53,57,59,70,73,97,99,101,102,103,104,105,107,109,133,135,140,143,144,145,146,147,],[16,16,-4,-5,-6,-7,-8,-9,-10,-11,-12,16,16,-25,-26,-27,-35,-36,-37,-34,-32,-22,-28,-30,-31,-13,-14,-15,-16,-17,16,16,-20,-24,-29,16,-23,-19,-18,-21,]),'BREAK':([0,3,4,5,6,7,8,9,10,11,12,21,30,33,34,35,46,52,53,57,59,70,73,97,99,101,102,103,104,105,107,109,133,135,140,143,144,145,146,147,],[17,17,-4,-5,-6,-7,-8,-9,-10,-11,-12,17,17,-25,-26,-27,-35,-36,-37,-34,-32,-22,-28,-30,-31,-13,-14,-15,-16,-17,17,17,-20,-24,-29,17,-23,-19,-18,-21,]),'CONTINUE':([0,3,4,5,6,7,8,9,10,11,12,21,30,33,34,35,46,52,53,57,59,70,73,97,99,101,102,103,104,105,107,109,133,135,140,143,144,145,146,147,],[18,18,-4,-5,-6,-7,-8,-9,-10,-11,-12,18,18,-25,-26,-27,-35,-36,-37,-34,-32,-22,-28,-30,-31,-13,-14,-15,-16,-17,18,18,-20,-24,-29,18,-23,-19,-18,-21,]),'RETURN':([0,3,4,5,6,7,8,9,10,11,12,21,30,33,34,35,46,52,53,57,59,70,73,97,99,101,102,103,104,105,107,109,133,135,140,143,144,145,146,147,],[19,19,-4,-5,-6,-7,-8,-9,-10,-11,-12,19,19,-25,-26,-27,-35,-36,-37,-34,-32,-22,-28,-30,-31,-13,-14,-15,-16,-17,19,19,-20,-24,-29,19,-23,-19,-18,-21,]),'PRINT':([0,3,4,5,6,7,8,9,10,11,12,21,30,33,34,35,46,52,53,57,59,70,73,97,99,101,102,103,104,105,107,109,133,135,140,143,144,145,146,147,],[20,20,-4,-5,-6,-7,-8,-9,-10,-11,-12,20,20,-25,-26,-27,-35,-36,-37,-34,-32,-22,-28,-30,-31,-13,-14,-15,-16,-17,20,20,-20,-24,-29,20,-23,-19,-18,-21,]),'{':([0,3,4,5,6,7,8,9,10,11,12,21,30,33,34,35,46,52,53,57,59,70,73,97,99,101,102,103,104,105,107,109,133,135,140,143,144,145,146,147,],[21,21,-4,-5,-6,-7,-8,-9,-10,-11,-12,21,21,-25,-26,-27,-35,-36,-37,-34,-32,-22,-28,-30,-31,-13,-14,-15,-16,-17,21,21,-20,-24,-29,21,-23,-19,-18,-21,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,22,33,34,35,59,70,73,97,99,101,102,103,104,105,133,135,140,145,146,147,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-3,-25,-26,-27,-32,-22,-28,-30,-31,-13,-14,-15,-16,-17,-20,-24,-29,-19,-18,-21,]),'}':([2,3,4,5,6,7,8,9,10,11,12,21,22,33,34,35,58,59,70,73,97,99,101,102,103,104,105,133,135,140,145,146,147,],[-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,59,-3,-25,-26,-27,99,-32,-22,-28,-30,-31,-13,-14,-15,-16,-17,-20,-24,-29,-19,-18,-21,]),'ELSE':([4,5,6,7,8,9,10,11,12,33,34,35,59,70,73,97,99,101,102,103,104,105,133,135,140,145,146,147,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-25,-26,-27,-32,-22,-28,-30,-31,-13,-14,-15,-16,-17,143,-24,-29,-19,-18,-21,]),'=':([13,31,106,],[23,71,132,]),'ADDASSIGN':([13,],[24,]),'SUBASSIGN':([13,],[25,]),'MULASSIGN':([13,],[26,]),'DIVASSIGN':([13,],[27,]),'[':([13,19,23,24,25,26,27,29,32,47,54,60,74,75,76,77,78,79,80,81,82,83,84,85,86,87,132,],[28,51,51,51,51,51,51,51,51,51,51,100,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'(':([14,16,48,49,50,],[29,32,90,91,92,]),';':([17,18,19,36,37,38,39,40,41,42,43,44,45,46,52,53,55,56,57,60,61,62,63,64,65,88,89,93,95,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,129,130,136,137,138,141,142,],[33,34,35,73,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,97,-70,-34,-34,101,102,103,104,105,-55,-54,-65,128,-46,-47,-48,-49,-50,-51,-52,-53,-56,-57,-58,-59,-60,-61,-66,140,-69,-62,-63,-64,145,146,]),'MINUS':([19,23,24,25,26,27,29,32,36,37,38,39,40,41,42,43,44,45,46,47,52,53,54,60,61,62,63,64,65,68,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,132,136,137,138,142,],[47,47,47,47,47,47,47,47,75,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,47,-36,-37,47,-34,75,75,75,75,75,-43,75,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-55,-54,-65,75,-46,-47,-48,-49,-50,-51,-52,-53,75,75,75,75,75,75,-66,47,-62,-63,-64,75,]),'ZEROS':([19,23,24,25,26,27,29,32,47,54,74,75,76,77,78,79,80,81,82,83,84,85,86,87,132,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'EYE':([19,23,24,25,26,27,29,32,47,54,74,75,76,77,78,79,80,81,82,83,84,85,86,87,132,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'ONES':([19,23,24,25,26,27,29,32,47,54,74,75,76,77,78,79,80,81,82,83,84,85,86,87,132,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'INTNUM':([19,20,23,24,25,26,27,28,29,32,47,51,54,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,91,92,98,100,128,132,134,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'FLOATNUM':([19,20,23,24,25,26,27,28,29,32,47,51,54,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,91,92,98,100,128,132,134,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'DOUBLEAPOSTROPHE':([20,37,38,39,40,41,42,43,44,45,46,52,53,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,],[54,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-55,-54,-65,129,-46,-47,-48,-49,-50,-51,-52,-53,-56,-57,-58,-59,-60,-61,-66,-62,-63,-64,]),'PLUS':([36,37,38,39,40,41,42,43,44,45,46,52,53,60,61,62,63,64,65,68,69,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,142,],[74,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,74,74,74,74,74,-43,74,-55,-54,-65,74,-46,-47,-48,-49,-50,-51,-52,-53,74,74,74,74,74,74,-66,-62,-63,-64,74,]),'TIMES':([36,37,38,39,40,41,42,43,44,45,46,52,53,60,61,62,63,64,65,68,69,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,142,],[76,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,76,76,76,76,76,-43,76,-55,-54,-65,76,76,76,-48,-49,76,76,-52,-53,76,76,76,76,76,76,-66,-62,-63,-64,76,]),'DIVIDE':([36,37,38,39,40,41,42,43,44,45,46,52,53,60,61,62,63,64,65,68,69,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,142,],[77,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,77,77,77,77,77,-43,77,-55,-54,-65,77,77,77,-48,-49,77,77,-52,-53,77,77,77,77,77,77,-66,-62,-63,-64,77,]),'DOTADD':([36,37,38,39,40,41,42,43,44,45,46,52,53,60,61,62,63,64,65,68,69,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,142,],[78,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,78,78,78,78,78,-43,78,-55,-54,-65,78,-46,-47,-48,-49,-50,-51,-52,-53,78,78,78,78,78,78,-66,-62,-63,-64,78,]),'DOTSUB':([36,37,38,39,40,41,42,43,44,45,46,52,53,60,61,62,63,64,65,68,69,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,142,],[79,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,79,79,79,79,79,-43,79,-55,-54,-65,79,-46,-47,-48,-49,-50,-51,-52,-53,79,79,79,79,79,79,-66,-62,-63,-64,79,]),'DOTMUL':([36,37,38,39,40,41,42,43,44,45,46,52,53,60,61,62,63,64,65,68,69,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,142,],[80,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,80,80,80,80,80,-43,80,-55,-54,-65,80,80,80,-48,-49,80,80,-52,-53,80,80,80,80,80,80,-66,-62,-63,-64,80,]),'DOTDIV':([36,37,38,39,40,41,42,43,44,45,46,52,53,60,61,62,63,64,65,68,69,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,142,],[81,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,81,81,81,81,81,-43,81,-55,-54,-65,81,81,81,-48,-49,81,81,-52,-53,81,81,81,81,81,81,-66,-62,-63,-64,81,]),'LESS_THAN':([36,37,38,39,40,41,42,43,44,45,46,52,53,60,61,62,63,64,65,68,69,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,142,],[82,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,82,82,82,82,82,-43,82,-55,-54,-65,82,-46,-47,-48,-49,-50,-51,-52,-53,None,None,None,None,None,None,-66,-62,-63,-64,82,]),'GREATER_THAN':([36,37,38,39,40,41,42,43,44,45,46,52,53,60,61,62,63,64,65,68,69,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,142,],[83,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,83,83,83,83,83,-43,83,-55,-54,-65,83,-46,-47,-48,-49,-50,-51,-52,-53,None,None,None,None,None,None,-66,-62,-63,-64,83,]),'LESS_OR_EQUAL_THAN':([36,37,38,39,40,41,42,43,44,45,46,52,53,60,61,62,63,64,65,68,69,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,142,],[84,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,84,84,84,84,84,-43,84,-55,-54,-65,84,-46,-47,-48,-49,-50,-51,-52,-53,None,None,None,None,None,None,-66,-62,-63,-64,84,]),'GREATER_OR_EQUAL_THAN':([36,37,38,39,40,41,42,43,44,45,46,52,53,60,61,62,63,64,65,68,69,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,142,],[85,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,85,85,85,85,85,-43,85,-55,-54,-65,85,-46,-47,-48,-49,-50,-51,-52,-53,None,None,None,None,None,None,-66,-62,-63,-64,85,]),'NOT_EQUAL':([36,37,38,39,40,41,42,43,44,45,46,52,53,60,61,62,63,64,65,68,69,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,142,],[86,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,86,86,86,86,86,-43,86,-55,-54,-65,86,-46,-47,-48,-49,-50,-51,-52,-53,None,None,None,None,None,None,-66,-62,-63,-64,86,]),'EQUAL':([36,37,38,39,40,41,42,43,44,45,46,52,53,60,61,62,63,64,65,68,69,88,89,93,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,136,137,138,142,],[87,-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,87,87,87,87,87,-43,87,-55,-54,-65,87,-46,-47,-48,-49,-50,-51,-52,-53,None,None,None,None,None,None,-66,-62,-63,-64,87,]),')':([37,38,39,40,41,42,43,44,45,46,52,53,57,67,68,72,88,89,93,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,136,137,138,],[-38,-39,-40,-41,-42,-43,-44,-45,-34,-35,-36,-37,-34,107,-33,109,-55,-54,-65,-46,-47,-48,-49,-50,-51,-52,-53,-56,-57,-58,-59,-60,-61,136,137,138,-66,-62,-63,-64,]),'APOSTROPHE':([45,60,],[88,88,]),',':([46,52,53,56,57,],[-35,-36,-37,98,-34,]),']':([46,51,52,53,56,57,66,94,95,130,131,139,],[-35,93,-36,-37,-70,-34,106,127,-68,-69,141,-67,]),':':([46,52,53,57,108,],[-35,-36,-37,-34,134,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,21,],[1,58,]),'instructions':([0,3,21,],[2,22,2,]),'instruction':([0,3,21,30,107,109,143,],[3,3,3,70,133,135,147,]),'assignment':([0,3,21,30,107,109,143,],[4,4,4,4,4,4,4,]),'ifx':([0,3,21,30,107,109,143,],[5,5,5,5,5,5,5,]),'if_else':([0,3,21,30,107,109,143,],[6,6,6,6,6,6,6,]),'for':([0,3,21,30,107,109,143,],[7,7,7,7,7,7,7,]),'while':([0,3,21,30,107,109,143,],[8,8,8,8,8,8,8,]),'command':([0,3,21,30,107,109,143,],[9,9,9,9,9,9,9,]),'return':([0,3,21,30,107,109,143,],[10,10,10,10,10,10,10,]),'print':([0,3,21,30,107,109,143,],[11,11,11,11,11,11,11,]),'compound':([0,3,21,30,107,109,143,],[12,12,12,12,12,12,12,]),'iterator':([15,],[30,]),'expression':([19,23,24,25,26,27,29,32,47,54,74,75,76,77,78,79,80,81,82,83,84,85,86,87,132,],[36,61,62,63,64,65,69,69,89,96,110,111,112,113,114,115,116,117,118,119,120,121,122,123,142,]),'factor':([19,20,23,24,25,26,27,28,29,32,47,51,54,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,91,92,98,100,128,132,134,],[37,56,37,37,37,37,37,56,37,37,37,56,37,108,37,37,37,37,37,37,37,37,37,37,37,37,37,37,124,125,126,56,56,56,37,144,]),'expression_bin_op':([19,23,24,25,26,27,29,32,47,54,74,75,76,77,78,79,80,81,82,83,84,85,86,87,132,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'expression_dot_bin_op':([19,23,24,25,26,27,29,32,47,54,74,75,76,77,78,79,80,81,82,83,84,85,86,87,132,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'expression_uminus':([19,23,24,25,26,27,29,32,47,54,74,75,76,77,78,79,80,81,82,83,84,85,86,87,132,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'expression_transposition':([19,23,24,25,26,27,29,32,47,54,74,75,76,77,78,79,80,81,82,83,84,85,86,87,132,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'expression_comparison':([19,23,24,25,26,27,29,32,47,54,74,75,76,77,78,79,80,81,82,83,84,85,86,87,132,],[42,42,42,42,42,42,68,68,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'expression_matrix':([19,23,24,25,26,27,29,32,47,54,74,75,76,77,78,79,80,81,82,83,84,85,86,87,132,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'expression_table':([19,23,24,25,26,27,29,32,47,54,74,75,76,77,78,79,80,81,82,83,84,85,86,87,132,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'number':([19,20,23,24,25,26,27,28,29,32,47,51,54,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,91,92,98,100,128,132,134,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'vector':([20,28,51,98,100,128,],[55,66,95,130,131,95,]),'condition':([29,32,],[67,72,]),'matrix':([51,128,],[94,139,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions','program',1,'p_program','my_parser.py',28),
  ('instructions -> instruction','instructions',1,'p_instructions','my_parser.py',34),
  ('instructions -> instruction instructions','instructions',2,'p_instructions','my_parser.py',35),
  ('instruction -> assignment','instruction',1,'p_instruction','my_parser.py',43),
  ('instruction -> ifx','instruction',1,'p_instruction','my_parser.py',44),
  ('instruction -> if_else','instruction',1,'p_instruction','my_parser.py',45),
  ('instruction -> for','instruction',1,'p_instruction','my_parser.py',46),
  ('instruction -> while','instruction',1,'p_instruction','my_parser.py',47),
  ('instruction -> command','instruction',1,'p_instruction','my_parser.py',48),
  ('instruction -> return','instruction',1,'p_instruction','my_parser.py',49),
  ('instruction -> print','instruction',1,'p_instruction','my_parser.py',50),
  ('instruction -> compound','instruction',1,'p_instruction','my_parser.py',51),
  ('assignment -> ID = expression ;','assignment',4,'p_assignment','my_parser.py',56),
  ('assignment -> ID ADDASSIGN expression ;','assignment',4,'p_assignment','my_parser.py',57),
  ('assignment -> ID SUBASSIGN expression ;','assignment',4,'p_assignment','my_parser.py',58),
  ('assignment -> ID MULASSIGN expression ;','assignment',4,'p_assignment','my_parser.py',59),
  ('assignment -> ID DIVASSIGN expression ;','assignment',4,'p_assignment','my_parser.py',60),
  ('assignment -> ID [ vector ] = expression ;','assignment',7,'p_assignment','my_parser.py',61),
  ('assignment -> ID = ID [ vector ] ;','assignment',7,'p_assignment_refference','my_parser.py',80),
  ('ifx -> IF ( condition ) instruction','ifx',5,'p_ifx','my_parser.py',100),
  ('if_else -> IF ( condition ) instruction ELSE instruction','if_else',7,'p_if_else','my_parser.py',105),
  ('for -> FOR iterator instruction','for',3,'p_for','my_parser.py',110),
  ('iterator -> ID = factor : factor','iterator',5,'p_iterator','my_parser.py',115),
  ('while -> WHILE ( condition ) instruction','while',5,'p_while','my_parser.py',120),
  ('command -> BREAK ;','command',2,'p_command','my_parser.py',125),
  ('command -> CONTINUE ;','command',2,'p_command','my_parser.py',126),
  ('return -> RETURN ;','return',2,'p_return','my_parser.py',131),
  ('return -> RETURN expression ;','return',3,'p_return_expression','my_parser.py',136),
  ('print -> PRINT DOUBLEAPOSTROPHE expression DOUBLEAPOSTROPHE ;','print',5,'p_print','my_parser.py',141),
  ('print -> PRINT vector ;','print',3,'p_print','my_parser.py',142),
  ('compound -> { program }','compound',3,'p_compound','my_parser.py',149),
  ('compound -> { }','compound',2,'p_compound','my_parser.py',150),
  ('condition -> expression_comparison','condition',1,'p_condition','my_parser.py',156),
  ('factor -> ID','factor',1,'p_variable_factor','my_parser.py',161),
  ('factor -> number','factor',1,'p_numerical_factor','my_parser.py',166),
  ('number -> INTNUM','number',1,'p_int_number','my_parser.py',171),
  ('number -> FLOATNUM','number',1,'p_float_number','my_parser.py',176),
  ('expression -> factor','expression',1,'p_expression','my_parser.py',181),
  ('expression -> expression_bin_op','expression',1,'p_expression','my_parser.py',182),
  ('expression -> expression_dot_bin_op','expression',1,'p_expression','my_parser.py',183),
  ('expression -> expression_uminus','expression',1,'p_expression','my_parser.py',184),
  ('expression -> expression_transposition','expression',1,'p_expression','my_parser.py',185),
  ('expression -> expression_comparison','expression',1,'p_expression','my_parser.py',186),
  ('expression -> expression_matrix','expression',1,'p_expression','my_parser.py',187),
  ('expression -> expression_table','expression',1,'p_expression','my_parser.py',188),
  ('expression_bin_op -> expression PLUS expression','expression_bin_op',3,'p_expression_bin_op','my_parser.py',193),
  ('expression_bin_op -> expression MINUS expression','expression_bin_op',3,'p_expression_bin_op','my_parser.py',194),
  ('expression_bin_op -> expression TIMES expression','expression_bin_op',3,'p_expression_bin_op','my_parser.py',195),
  ('expression_bin_op -> expression DIVIDE expression','expression_bin_op',3,'p_expression_bin_op','my_parser.py',196),
  ('expression_dot_bin_op -> expression DOTADD expression','expression_dot_bin_op',3,'p_expression_dot_bin_op','my_parser.py',201),
  ('expression_dot_bin_op -> expression DOTSUB expression','expression_dot_bin_op',3,'p_expression_dot_bin_op','my_parser.py',202),
  ('expression_dot_bin_op -> expression DOTMUL expression','expression_dot_bin_op',3,'p_expression_dot_bin_op','my_parser.py',203),
  ('expression_dot_bin_op -> expression DOTDIV expression','expression_dot_bin_op',3,'p_expression_dot_bin_op','my_parser.py',204),
  ('expression_uminus -> MINUS expression','expression_uminus',2,'p_expression_uminus','my_parser.py',209),
  ('expression_transposition -> ID APOSTROPHE','expression_transposition',2,'p_expression_transposition','my_parser.py',214),
  ('expression_comparison -> expression LESS_THAN expression','expression_comparison',3,'p_expression_comparison','my_parser.py',219),
  ('expression_comparison -> expression GREATER_THAN expression','expression_comparison',3,'p_expression_comparison','my_parser.py',220),
  ('expression_comparison -> expression LESS_OR_EQUAL_THAN expression','expression_comparison',3,'p_expression_comparison','my_parser.py',221),
  ('expression_comparison -> expression GREATER_OR_EQUAL_THAN expression','expression_comparison',3,'p_expression_comparison','my_parser.py',222),
  ('expression_comparison -> expression NOT_EQUAL expression','expression_comparison',3,'p_expression_comparison','my_parser.py',223),
  ('expression_comparison -> expression EQUAL expression','expression_comparison',3,'p_expression_comparison','my_parser.py',224),
  ('expression_matrix -> ZEROS ( factor )','expression_matrix',4,'p_expression_matrix','my_parser.py',229),
  ('expression_matrix -> EYE ( factor )','expression_matrix',4,'p_expression_matrix','my_parser.py',230),
  ('expression_matrix -> ONES ( factor )','expression_matrix',4,'p_expression_matrix','my_parser.py',231),
  ('expression_table -> [ ]','expression_table',2,'p_empty_list','my_parser.py',236),
  ('expression_table -> [ matrix ]','expression_table',3,'p_non_empty_matrix','my_parser.py',242),
  ('matrix -> vector ; matrix','matrix',3,'p_matrix','my_parser.py',249),
  ('matrix -> vector','matrix',1,'p_matrix','my_parser.py',250),
  ('vector -> factor , vector','vector',3,'p_vector','my_parser.py',260),
  ('vector -> factor','vector',1,'p_vector','my_parser.py',261),
]