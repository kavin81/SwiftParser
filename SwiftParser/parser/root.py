def p_statements(p):
    """statements : statement
    | statements statement"""
    if len(p) == 2:
        if p[1]:
            p[0] = [p[1]]
        else:
            p[0] = []
    else:
        p[0] = p[1] + [p[2]]


def p_statement(p):
    """statement : data_declaration
    | func_declaration
    | expression
    | if_statement
    | for_statement
    | while_statement"""
    p[0] = p[1]


def p_data_declaration(p):
    """data_declaration : LET IDENTIFIER COLON typehint EQUAL expression
    | VAR IDENTIFIER COLON typehint EQUAL expression
    | IDENTIFIER EQUAL expression
    """
    if len(p) == 7:
        p[0] = ("data_declaration", p[1], p[2], p[4], p[6])
    elif len(p) == 6:
        p[0] = ("data_declaration", p[1], p[2], p[4], p[6])
    else:
        p[0] = ("data_declaration", p[1], p[3])


def p_func_declaration(p):
    """func_declaration : FUNC IDENTIFIER LPAREN RPAREN RARROW typehint LBRACE statements RBRACE
    | FUNC IDENTIFIER LPAREN func_params RPAREN RARROW typehint LBRACE statements RBRACE
    | FUNC IDENTIFIER LPAREN RPAREN LBRACE statements RBRACE
    | FUNC IDENTIFIER LPAREN func_params RPAREN LBRACE statements RBRACE"""
    if len(p) == 10:
        p[0] = ("func_declaration", p[2], p[6], p[8])
    elif len(p) == 11:
        p[0] = ("func_declaration", p[2], p[4], p[7], p[9])
    elif len(p) == 8:
        p[0] = ("func_declaration", p[2], p[6])
    else:
        p[0] = ("func_declaration", p[2], p[4], p[7])


def p_func_params(p):
    """func_params : func_param
    | func_params COMMA func_param"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_func_param(p):
    """func_param : IDENTIFIER COLON typehint"""
    p[0] = (p[1], p[3])


def p_expression(p):
    """expression : IDENTIFIER
    | basic_types
    | comparison_expression"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2], p[3])


def p_comparison_expression(p):
    """comparison_expression : expression bin_operators expression"""
    p[0] = (p[1], p[2], p[3])
