
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL BOOL_TYPE COLON COMMA DIVIDE DOT ELIF ELSE EQEQ EQUAL FLOAT FLOAT_TYPE FOR FUNC GREATER GREATER_EQUAL IDENTIFIER IF IN INT INT_TYPE LBRACE LBRACKET LESS LESS_EQUAL LET LPAREN MINUS MOD NOT_EQUAL OR PLUS RARROW RBRACE RBRACKET REPEAT RPAREN SET_TYPE STRING STRING_TYPE TIMES VAR WHILEstatements : statement\n| statements statementif_statement : IF LPAREN expression RPAREN LBRACE statements RBRACE elifs else_statementbin_operators : PLUS\n| MINUS\n| TIMES\n| DIVIDE\n| MOD\n| EQEQ\n| NOT_EQUAL\n| LESS\n| LESS_EQUAL\n| GREATER\n| GREATER_EQUAL\n| AND\n| ORfor_statement : FOR IDENTIFIER IN for_sequence LBRACE statements RBRACEempty :elifs : elifs ELIF LPAREN expression RPAREN LBRACE statements RBRACE\n| emptyfor_sequence : IDENTIFIER\n| collections\n| INT DOT DOT INTstatement : data_declaration\n| func_declaration\n| expression\n| if_statement\n| for_statement\n| while_statementelse_statement : ELSE LBRACE statements RBRACE\n| emptywhile_block : WHILE LPAREN expression RPARENbasic_typehints : INT_TYPE\n| FLOAT_TYPE\n| BOOL_TYPE\n| STRING_TYPE\n| SET_TYPEdata_declaration : LET IDENTIFIER COLON typehint EQUAL expression\n| VAR IDENTIFIER COLON typehint EQUAL expression\n| IDENTIFIER EQUAL expression\nwhile_statement : while_block LBRACE statements RBRACE\n| REPEAT LBRACE statements RBRACE while_blocktypehint : LBRACKET basic_typehints RBRACKET\n| LBRACKET basic_typehints COLON basic_typehints RBRACKET\n| basic_typehintsfunc_declaration : FUNC IDENTIFIER LPAREN RPAREN RARROW typehint LBRACE statements RBRACE\n| FUNC IDENTIFIER LPAREN func_params RPAREN RARROW typehint LBRACE statements RBRACE\n| FUNC IDENTIFIER LPAREN RPAREN LBRACE statements RBRACE\n| FUNC IDENTIFIER LPAREN func_params RPAREN LBRACE statements RBRACEbasic_types : INT\n| FLOAT\n| BOOL\n| STRING\n| collectionsfunc_params : func_param\n| func_params COMMA func_paramfunc_param : IDENTIFIER COLON typehintcollections : LBRACKET collection_contents RBRACKET\n| LPAREN collection_contents RPARENexpression : IDENTIFIER\n| basic_types\n| comparison_expressioncollection_contents : collection_content\n| collection_content COMMA collection_contentscomparison_expression : expression bin_operators expressioncollection_content : basic_types\n| basic_types COLON basic_types'
    
_lr_action_items = {'LET':([0,1,2,3,4,5,6,7,8,10,14,15,20,21,22,23,24,27,51,52,55,56,58,61,66,67,69,90,92,98,101,102,104,105,108,111,113,115,116,119,120,122,123,124,127,128,129,130,131,132,133,134,137,138,140,142,144,145,146,147,],[9,9,-1,-24,-25,-26,-27,-28,-29,-60,-61,-62,-50,-51,-52,-53,-54,-2,9,9,-65,-60,-40,-59,9,9,-58,-41,-32,9,9,9,-42,-38,-39,9,9,9,9,9,-48,9,-18,-17,9,9,-49,-18,-20,-46,9,-3,-31,-47,9,9,-30,9,9,-19,]),'VAR':([0,1,2,3,4,5,6,7,8,10,14,15,20,21,22,23,24,27,51,52,55,56,58,61,66,67,69,90,92,98,101,102,104,105,108,111,113,115,116,119,120,122,123,124,127,128,129,130,131,132,133,134,137,138,140,142,144,145,146,147,],[11,11,-1,-24,-25,-26,-27,-28,-29,-60,-61,-62,-50,-51,-52,-53,-54,-2,11,11,-65,-60,-40,-59,11,11,-58,-41,-32,11,11,11,-42,-38,-39,11,11,11,11,11,-48,11,-18,-17,11,11,-49,-18,-20,-46,11,-3,-31,-47,11,11,-30,11,11,-19,]),'IDENTIFIER':([0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,17,20,21,22,23,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,49,51,52,53,55,56,58,60,61,65,66,67,69,90,92,93,95,98,100,101,102,104,105,108,111,113,115,116,119,120,122,123,124,127,128,129,130,131,132,133,134,137,138,139,140,142,144,145,146,147,],[10,10,-1,-24,-25,-26,-27,-28,-29,42,-60,44,45,-61,-62,50,-50,-51,-52,-53,-54,-2,56,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,56,56,10,10,56,-65,-60,-40,79,-59,86,10,10,-58,-41,-32,56,56,10,79,10,10,-42,-38,-39,10,10,10,10,10,-48,10,-18,-17,10,10,-49,-18,-20,-46,10,-3,-31,-47,56,10,10,-30,10,10,-19,]),'FUNC':([0,1,2,3,4,5,6,7,8,10,14,15,20,21,22,23,24,27,51,52,55,56,58,61,66,67,69,90,92,98,101,102,104,105,108,111,113,115,116,119,120,122,123,124,127,128,129,130,131,132,133,134,137,138,140,142,144,145,146,147,],[12,12,-1,-24,-25,-26,-27,-28,-29,-60,-61,-62,-50,-51,-52,-53,-54,-2,12,12,-65,-60,-40,-59,12,12,-58,-41,-32,12,12,12,-42,-38,-39,12,12,12,12,12,-48,12,-18,-17,12,12,-49,-18,-20,-46,12,-3,-31,-47,12,12,-30,12,12,-19,]),'IF':([0,1,2,3,4,5,6,7,8,10,14,15,20,21,22,23,24,27,51,52,55,56,58,61,66,67,69,90,92,98,101,102,104,105,108,111,113,115,116,119,120,122,123,124,127,128,129,130,131,132,133,134,137,138,140,142,144,145,146,147,],[16,16,-1,-24,-25,-26,-27,-28,-29,-60,-61,-62,-50,-51,-52,-53,-54,-2,16,16,-65,-60,-40,-59,16,16,-58,-41,-32,16,16,16,-42,-38,-39,16,16,16,16,16,-48,16,-18,-17,16,16,-49,-18,-20,-46,16,-3,-31,-47,16,16,-30,16,16,-19,]),'FOR':([0,1,2,3,4,5,6,7,8,10,14,15,20,21,22,23,24,27,51,52,55,56,58,61,66,67,69,90,92,98,101,102,104,105,108,111,113,115,116,119,120,122,123,124,127,128,129,130,131,132,133,134,137,138,140,142,144,145,146,147,],[17,17,-1,-24,-25,-26,-27,-28,-29,-60,-61,-62,-50,-51,-52,-53,-54,-2,17,17,-65,-60,-40,-59,17,17,-58,-41,-32,17,17,17,-42,-38,-39,17,17,17,17,17,-48,17,-18,-17,17,17,-49,-18,-20,-46,17,-3,-31,-47,17,17,-30,17,17,-19,]),'REPEAT':([0,1,2,3,4,5,6,7,8,10,14,15,20,21,22,23,24,27,51,52,55,56,58,61,66,67,69,90,92,98,101,102,104,105,108,111,113,115,116,119,120,122,123,124,127,128,129,130,131,132,133,134,137,138,140,142,144,145,146,147,],[19,19,-1,-24,-25,-26,-27,-28,-29,-60,-61,-62,-50,-51,-52,-53,-54,-2,19,19,-65,-60,-40,-59,19,19,-58,-41,-32,19,19,19,-42,-38,-39,19,19,19,19,19,-48,19,-18,-17,19,19,-49,-18,-20,-46,19,-3,-31,-47,19,19,-30,19,19,-19,]),'INT':([0,1,2,3,4,5,6,7,8,10,13,14,15,20,21,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,49,51,52,53,55,56,58,61,62,63,65,66,67,69,90,92,93,95,98,101,102,104,105,108,111,113,115,116,117,119,120,122,123,124,127,128,129,130,131,132,133,134,137,138,139,140,142,144,145,146,147,],[20,20,-1,-24,-25,-26,-27,-28,-29,-60,20,-61,-62,-50,-51,-52,-53,-54,20,-2,20,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,20,20,20,20,20,-65,-60,-40,-59,20,20,89,20,20,-58,-41,-32,20,20,20,20,20,-42,-38,-39,20,20,20,20,125,20,-48,20,-18,-17,20,20,-49,-18,-20,-46,20,-3,-31,-47,20,20,20,-30,20,20,-19,]),'FLOAT':([0,1,2,3,4,5,6,7,8,10,13,14,15,20,21,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,49,51,52,53,55,56,58,61,62,63,66,67,69,90,92,93,95,98,101,102,104,105,108,111,113,115,116,119,120,122,123,124,127,128,129,130,131,132,133,134,137,138,139,140,142,144,145,146,147,],[21,21,-1,-24,-25,-26,-27,-28,-29,-60,21,-61,-62,-50,-51,-52,-53,-54,21,-2,21,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,21,21,21,21,21,-65,-60,-40,-59,21,21,21,21,-58,-41,-32,21,21,21,21,21,-42,-38,-39,21,21,21,21,21,-48,21,-18,-17,21,21,-49,-18,-20,-46,21,-3,-31,-47,21,21,21,-30,21,21,-19,]),'BOOL':([0,1,2,3,4,5,6,7,8,10,13,14,15,20,21,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,49,51,52,53,55,56,58,61,62,63,66,67,69,90,92,93,95,98,101,102,104,105,108,111,113,115,116,119,120,122,123,124,127,128,129,130,131,132,133,134,137,138,139,140,142,144,145,146,147,],[22,22,-1,-24,-25,-26,-27,-28,-29,-60,22,-61,-62,-50,-51,-52,-53,-54,22,-2,22,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,22,22,22,22,22,-65,-60,-40,-59,22,22,22,22,-58,-41,-32,22,22,22,22,22,-42,-38,-39,22,22,22,22,22,-48,22,-18,-17,22,22,-49,-18,-20,-46,22,-3,-31,-47,22,22,22,-30,22,22,-19,]),'STRING':([0,1,2,3,4,5,6,7,8,10,13,14,15,20,21,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,49,51,52,53,55,56,58,61,62,63,66,67,69,90,92,93,95,98,101,102,104,105,108,111,113,115,116,119,120,122,123,124,127,128,129,130,131,132,133,134,137,138,139,140,142,144,145,146,147,],[23,23,-1,-24,-25,-26,-27,-28,-29,-60,23,-61,-62,-50,-51,-52,-53,-54,23,-2,23,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,23,23,23,23,23,-65,-60,-40,-59,23,23,23,23,-58,-41,-32,23,23,23,23,23,-42,-38,-39,23,23,23,23,23,-48,23,-18,-17,23,23,-49,-18,-20,-46,23,-3,-31,-47,23,23,23,-30,23,23,-19,]),'WHILE':([0,1,2,3,4,5,6,7,8,10,14,15,20,21,22,23,24,27,51,52,55,56,58,61,66,67,69,90,91,92,98,101,102,104,105,108,111,113,115,116,119,120,122,123,124,127,128,129,130,131,132,133,134,137,138,140,142,144,145,146,147,],[25,25,-1,-24,-25,-26,-27,-28,-29,-60,-61,-62,-50,-51,-52,-53,-54,-2,25,25,-65,-60,-40,-59,25,25,-58,-41,25,-32,25,25,25,-42,-38,-39,25,25,25,25,25,-48,25,-18,-17,25,25,-49,-18,-20,-46,25,-3,-31,-47,25,25,-30,25,25,-19,]),'LBRACKET':([0,1,2,3,4,5,6,7,8,10,13,14,15,20,21,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,49,51,52,53,55,56,57,58,59,61,62,63,65,66,67,69,90,92,93,95,96,97,98,101,102,104,105,108,111,112,113,115,116,119,120,122,123,124,127,128,129,130,131,132,133,134,137,138,139,140,142,144,145,146,147,],[26,26,-1,-24,-25,-26,-27,-28,-29,-60,26,-61,-62,-50,-51,-52,-53,-54,26,-2,26,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,26,26,26,26,26,-65,-60,71,-40,71,-59,26,26,26,26,26,-58,-41,-32,26,26,71,71,26,26,26,-42,-38,-39,26,71,26,26,26,26,-48,26,-18,-17,26,26,-49,-18,-20,-46,26,-3,-31,-47,26,26,26,-30,26,26,-19,]),'LPAREN':([0,1,2,3,4,5,6,7,8,10,13,14,15,16,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,45,49,51,52,53,55,56,58,61,62,63,65,66,67,69,90,92,93,95,98,101,102,104,105,108,111,113,115,116,119,120,122,123,124,127,128,129,130,131,132,133,134,135,137,138,139,140,142,144,145,146,147,],[13,13,-1,-24,-25,-26,-27,-28,-29,-60,13,-61,-62,49,-50,-51,-52,-53,-54,53,13,-2,13,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,13,60,13,13,13,13,-65,-60,-40,-59,13,13,13,13,13,-58,-41,-32,13,13,13,13,13,-42,-38,-39,13,13,13,13,13,-48,13,-18,-17,13,13,-49,-18,-20,-46,13,-3,139,-31,-47,13,13,13,-30,13,13,-19,]),'$end':([1,2,3,4,5,6,7,8,10,14,15,20,21,22,23,24,27,55,56,58,61,69,90,92,104,105,108,120,123,124,129,130,131,132,134,137,138,144,147,],[0,-1,-24,-25,-26,-27,-28,-29,-60,-61,-62,-50,-51,-52,-53,-54,-2,-65,-60,-40,-59,-58,-41,-32,-42,-38,-39,-48,-18,-17,-49,-18,-20,-46,-3,-31,-47,-30,-19,]),'RBRACE':([2,3,4,5,6,7,8,10,14,15,20,21,22,23,24,27,55,56,58,61,66,67,69,90,92,104,105,108,111,115,116,120,122,123,124,127,129,130,131,132,133,134,137,138,142,144,146,147,],[-1,-24,-25,-26,-27,-28,-29,-60,-61,-62,-50,-51,-52,-53,-54,-2,-65,-60,-40,-59,90,91,-58,-41,-32,-42,-38,-39,120,123,124,-48,129,-18,-17,132,-49,-18,-20,-46,138,-3,-31,-47,144,-30,147,-19,]),'PLUS':([5,10,14,15,20,21,22,23,24,55,56,58,61,64,68,69,105,108,141,],[29,-60,-61,-62,-50,-51,-52,-53,-54,29,-60,29,-59,29,29,-58,29,29,29,]),'MINUS':([5,10,14,15,20,21,22,23,24,55,56,58,61,64,68,69,105,108,141,],[30,-60,-61,-62,-50,-51,-52,-53,-54,30,-60,30,-59,30,30,-58,30,30,30,]),'TIMES':([5,10,14,15,20,21,22,23,24,55,56,58,61,64,68,69,105,108,141,],[31,-60,-61,-62,-50,-51,-52,-53,-54,31,-60,31,-59,31,31,-58,31,31,31,]),'DIVIDE':([5,10,14,15,20,21,22,23,24,55,56,58,61,64,68,69,105,108,141,],[32,-60,-61,-62,-50,-51,-52,-53,-54,32,-60,32,-59,32,32,-58,32,32,32,]),'MOD':([5,10,14,15,20,21,22,23,24,55,56,58,61,64,68,69,105,108,141,],[33,-60,-61,-62,-50,-51,-52,-53,-54,33,-60,33,-59,33,33,-58,33,33,33,]),'EQEQ':([5,10,14,15,20,21,22,23,24,55,56,58,61,64,68,69,105,108,141,],[34,-60,-61,-62,-50,-51,-52,-53,-54,34,-60,34,-59,34,34,-58,34,34,34,]),'NOT_EQUAL':([5,10,14,15,20,21,22,23,24,55,56,58,61,64,68,69,105,108,141,],[35,-60,-61,-62,-50,-51,-52,-53,-54,35,-60,35,-59,35,35,-58,35,35,35,]),'LESS':([5,10,14,15,20,21,22,23,24,55,56,58,61,64,68,69,105,108,141,],[36,-60,-61,-62,-50,-51,-52,-53,-54,36,-60,36,-59,36,36,-58,36,36,36,]),'LESS_EQUAL':([5,10,14,15,20,21,22,23,24,55,56,58,61,64,68,69,105,108,141,],[37,-60,-61,-62,-50,-51,-52,-53,-54,37,-60,37,-59,37,37,-58,37,37,37,]),'GREATER':([5,10,14,15,20,21,22,23,24,55,56,58,61,64,68,69,105,108,141,],[38,-60,-61,-62,-50,-51,-52,-53,-54,38,-60,38,-59,38,38,-58,38,38,38,]),'GREATER_EQUAL':([5,10,14,15,20,21,22,23,24,55,56,58,61,64,68,69,105,108,141,],[39,-60,-61,-62,-50,-51,-52,-53,-54,39,-60,39,-59,39,39,-58,39,39,39,]),'AND':([5,10,14,15,20,21,22,23,24,55,56,58,61,64,68,69,105,108,141,],[40,-60,-61,-62,-50,-51,-52,-53,-54,40,-60,40,-59,40,40,-58,40,40,40,]),'OR':([5,10,14,15,20,21,22,23,24,55,56,58,61,64,68,69,105,108,141,],[41,-60,-61,-62,-50,-51,-52,-53,-54,41,-60,41,-59,41,41,-58,41,41,41,]),'EQUAL':([10,70,72,73,74,75,76,77,78,106,126,],[43,93,-45,-33,-34,-35,-36,-37,95,-43,-44,]),'RPAREN':([14,15,20,21,22,23,24,46,47,48,55,56,60,61,64,68,69,72,73,74,75,76,77,81,82,83,84,106,109,114,126,141,],[-61,-62,-50,-51,-52,-53,-54,61,-63,-66,-65,-60,80,-59,85,92,-58,-45,-33,-34,-35,-36,-37,99,-55,-64,-67,-43,-57,-56,-44,143,]),'LBRACE':([18,19,61,69,72,73,74,75,76,77,80,85,86,87,88,92,99,106,110,121,125,126,136,143,],[51,52,-59,-58,-45,-33,-34,-35,-36,-37,98,101,-21,102,-22,-32,113,-43,119,128,-23,-44,140,145,]),'COLON':([20,21,22,23,24,42,44,48,61,69,73,74,75,76,77,79,94,],[-50,-51,-52,-53,-54,57,59,63,-59,-58,-33,-34,-35,-36,-37,96,107,]),'COMMA':([20,21,22,23,24,47,48,61,69,72,73,74,75,76,77,81,82,84,106,109,114,126,],[-50,-51,-52,-53,-54,62,-66,-59,-58,-45,-33,-34,-35,-36,-37,100,-55,-67,-43,-57,-56,-44,]),'RBRACKET':([20,21,22,23,24,47,48,54,61,69,73,74,75,76,77,83,84,94,118,],[-50,-51,-52,-53,-54,-63,-66,69,-59,-58,-33,-34,-35,-36,-37,-64,-67,106,126,]),'IN':([50,],[65,]),'INT_TYPE':([57,59,71,96,97,107,112,],[73,73,73,73,73,73,73,]),'FLOAT_TYPE':([57,59,71,96,97,107,112,],[74,74,74,74,74,74,74,]),'BOOL_TYPE':([57,59,71,96,97,107,112,],[75,75,75,75,75,75,75,]),'STRING_TYPE':([57,59,71,96,97,107,112,],[76,76,76,76,76,76,76,]),'SET_TYPE':([57,59,71,96,97,107,112,],[77,77,77,77,77,77,77,]),'RARROW':([80,99,],[97,112,]),'DOT':([89,103,],[103,117,]),'ELIF':([123,130,131,147,],[-18,135,-20,-19,]),'ELSE':([123,130,131,147,],[-18,136,-20,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,51,52,98,101,102,113,119,128,140,145,],[1,66,67,111,115,116,122,127,133,142,146,]),'statement':([0,1,51,52,66,67,98,101,102,111,113,115,116,119,122,127,128,133,140,142,145,146,],[2,27,2,2,27,27,2,2,2,27,2,27,27,2,27,27,2,27,2,27,2,27,]),'data_declaration':([0,1,51,52,66,67,98,101,102,111,113,115,116,119,122,127,128,133,140,142,145,146,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'func_declaration':([0,1,51,52,66,67,98,101,102,111,113,115,116,119,122,127,128,133,140,142,145,146,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'expression':([0,1,28,43,49,51,52,53,66,67,93,95,98,101,102,111,113,115,116,119,122,127,128,133,139,140,142,145,146,],[5,5,55,58,64,5,5,68,5,5,105,108,5,5,5,5,5,5,5,5,5,5,5,5,141,5,5,5,5,]),'if_statement':([0,1,51,52,66,67,98,101,102,111,113,115,116,119,122,127,128,133,140,142,145,146,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'for_statement':([0,1,51,52,66,67,98,101,102,111,113,115,116,119,122,127,128,133,140,142,145,146,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'while_statement':([0,1,51,52,66,67,98,101,102,111,113,115,116,119,122,127,128,133,140,142,145,146,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'basic_types':([0,1,13,26,28,43,49,51,52,53,62,63,66,67,93,95,98,101,102,111,113,115,116,119,122,127,128,133,139,140,142,145,146,],[14,14,48,48,14,14,14,14,14,14,48,84,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'comparison_expression':([0,1,28,43,49,51,52,53,66,67,93,95,98,101,102,111,113,115,116,119,122,127,128,133,139,140,142,145,146,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'while_block':([0,1,51,52,66,67,91,98,101,102,111,113,115,116,119,122,127,128,133,140,142,145,146,],[18,18,18,18,18,18,104,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'collections':([0,1,13,26,28,43,49,51,52,53,62,63,65,66,67,93,95,98,101,102,111,113,115,116,119,122,127,128,133,139,140,142,145,146,],[24,24,24,24,24,24,24,24,24,24,24,24,88,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'bin_operators':([5,55,58,64,68,105,108,141,],[28,28,28,28,28,28,28,28,]),'collection_contents':([13,26,62,],[46,54,83,]),'collection_content':([13,26,62,],[47,47,47,]),'typehint':([57,59,96,97,112,],[70,78,109,110,121,]),'basic_typehints':([57,59,71,96,97,107,112,],[72,72,94,72,72,118,72,]),'func_params':([60,],[81,]),'func_param':([60,100,],[82,114,]),'for_sequence':([65,],[87,]),'elifs':([123,],[130,]),'empty':([123,130,],[131,137,]),'else_statement':([130,],[134,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statement','statements',1,'p_statements','root.py',2),
  ('statements -> statements statement','statements',2,'p_statements','root.py',3),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE statements RBRACE elifs else_statement','if_statement',9,'p_if_statement','selection.py',2),
  ('bin_operators -> PLUS','bin_operators',1,'p_bin_operators','types.py',2),
  ('bin_operators -> MINUS','bin_operators',1,'p_bin_operators','types.py',3),
  ('bin_operators -> TIMES','bin_operators',1,'p_bin_operators','types.py',4),
  ('bin_operators -> DIVIDE','bin_operators',1,'p_bin_operators','types.py',5),
  ('bin_operators -> MOD','bin_operators',1,'p_bin_operators','types.py',6),
  ('bin_operators -> EQEQ','bin_operators',1,'p_bin_operators','types.py',7),
  ('bin_operators -> NOT_EQUAL','bin_operators',1,'p_bin_operators','types.py',8),
  ('bin_operators -> LESS','bin_operators',1,'p_bin_operators','types.py',9),
  ('bin_operators -> LESS_EQUAL','bin_operators',1,'p_bin_operators','types.py',10),
  ('bin_operators -> GREATER','bin_operators',1,'p_bin_operators','types.py',11),
  ('bin_operators -> GREATER_EQUAL','bin_operators',1,'p_bin_operators','types.py',12),
  ('bin_operators -> AND','bin_operators',1,'p_bin_operators','types.py',13),
  ('bin_operators -> OR','bin_operators',1,'p_bin_operators','types.py',14),
  ('for_statement -> FOR IDENTIFIER IN for_sequence LBRACE statements RBRACE','for_statement',7,'p_for_statement','loop.py',5),
  ('empty -> <empty>','empty',0,'p_empty','util.py',5),
  ('elifs -> elifs ELIF LPAREN expression RPAREN LBRACE statements RBRACE','elifs',8,'p_elifs','selection.py',7),
  ('elifs -> empty','elifs',1,'p_elifs','selection.py',8),
  ('for_sequence -> IDENTIFIER','for_sequence',1,'p_for_sequence','loop.py',10),
  ('for_sequence -> collections','for_sequence',1,'p_for_sequence','loop.py',11),
  ('for_sequence -> INT DOT DOT INT','for_sequence',4,'p_for_sequence','loop.py',12),
  ('statement -> data_declaration','statement',1,'p_statement','root.py',14),
  ('statement -> func_declaration','statement',1,'p_statement','root.py',15),
  ('statement -> expression','statement',1,'p_statement','root.py',16),
  ('statement -> if_statement','statement',1,'p_statement','root.py',17),
  ('statement -> for_statement','statement',1,'p_statement','root.py',18),
  ('statement -> while_statement','statement',1,'p_statement','root.py',19),
  ('else_statement -> ELSE LBRACE statements RBRACE','else_statement',4,'p_else_statement','selection.py',16),
  ('else_statement -> empty','else_statement',1,'p_else_statement','selection.py',17),
  ('while_block -> WHILE LPAREN expression RPAREN','while_block',4,'p_while_block','loop.py',20),
  ('basic_typehints -> INT_TYPE','basic_typehints',1,'p_basic_typehints','types.py',22),
  ('basic_typehints -> FLOAT_TYPE','basic_typehints',1,'p_basic_typehints','types.py',23),
  ('basic_typehints -> BOOL_TYPE','basic_typehints',1,'p_basic_typehints','types.py',24),
  ('basic_typehints -> STRING_TYPE','basic_typehints',1,'p_basic_typehints','types.py',25),
  ('basic_typehints -> SET_TYPE','basic_typehints',1,'p_basic_typehints','types.py',26),
  ('data_declaration -> LET IDENTIFIER COLON typehint EQUAL expression','data_declaration',6,'p_data_declaration','root.py',24),
  ('data_declaration -> VAR IDENTIFIER COLON typehint EQUAL expression','data_declaration',6,'p_data_declaration','root.py',25),
  ('data_declaration -> IDENTIFIER EQUAL expression','data_declaration',3,'p_data_declaration','root.py',26),
  ('while_statement -> while_block LBRACE statements RBRACE','while_statement',4,'p_while_statement','loop.py',25),
  ('while_statement -> REPEAT LBRACE statements RBRACE while_block','while_statement',5,'p_while_statement','loop.py',26),
  ('typehint -> LBRACKET basic_typehints RBRACKET','typehint',3,'p_typehint','types.py',31),
  ('typehint -> LBRACKET basic_typehints COLON basic_typehints RBRACKET','typehint',5,'p_typehint','types.py',32),
  ('typehint -> basic_typehints','typehint',1,'p_typehint','types.py',33),
  ('func_declaration -> FUNC IDENTIFIER LPAREN RPAREN RARROW typehint LBRACE statements RBRACE','func_declaration',9,'p_func_declaration','root.py',37),
  ('func_declaration -> FUNC IDENTIFIER LPAREN func_params RPAREN RARROW typehint LBRACE statements RBRACE','func_declaration',10,'p_func_declaration','root.py',38),
  ('func_declaration -> FUNC IDENTIFIER LPAREN RPAREN LBRACE statements RBRACE','func_declaration',7,'p_func_declaration','root.py',39),
  ('func_declaration -> FUNC IDENTIFIER LPAREN func_params RPAREN LBRACE statements RBRACE','func_declaration',8,'p_func_declaration','root.py',40),
  ('basic_types -> INT','basic_types',1,'p_basic_types','types.py',46),
  ('basic_types -> FLOAT','basic_types',1,'p_basic_types','types.py',47),
  ('basic_types -> BOOL','basic_types',1,'p_basic_types','types.py',48),
  ('basic_types -> STRING','basic_types',1,'p_basic_types','types.py',49),
  ('basic_types -> collections','basic_types',1,'p_basic_types','types.py',50),
  ('func_params -> func_param','func_params',1,'p_func_params','root.py',52),
  ('func_params -> func_params COMMA func_param','func_params',3,'p_func_params','root.py',53),
  ('func_param -> IDENTIFIER COLON typehint','func_param',3,'p_func_param','root.py',61),
  ('collections -> LBRACKET collection_contents RBRACKET','collections',3,'p_collections','types.py',62),
  ('collections -> LPAREN collection_contents RPAREN','collections',3,'p_collections','types.py',63),
  ('expression -> IDENTIFIER','expression',1,'p_expression','root.py',66),
  ('expression -> basic_types','expression',1,'p_expression','root.py',67),
  ('expression -> comparison_expression','expression',1,'p_expression','root.py',68),
  ('collection_contents -> collection_content','collection_contents',1,'p_collection_contents','types.py',68),
  ('collection_contents -> collection_content COMMA collection_contents','collection_contents',3,'p_collection_contents','types.py',69),
  ('comparison_expression -> expression bin_operators expression','comparison_expression',3,'p_comparison_expression','root.py',76),
  ('collection_content -> basic_types','collection_content',1,'p_collection_content','types.py',77),
  ('collection_content -> basic_types COLON basic_types','collection_content',3,'p_collection_content','types.py',78),
]
