def p_statements(p):
    """statements : statement
    | statements statement"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_statement(p):
    """statement : data_declaration
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
