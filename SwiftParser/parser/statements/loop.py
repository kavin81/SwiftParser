# for-in , while , repeat-while


def p_for_statement(p):
    """for_statement : FOR IDENTIFIER IN for_sequence LBRACE statements RBRACE"""
    p[0] = ("for", p[2], p[4], p[6])


def p_for_sequence(p):
    """for_sequence : IDENTIFIER
    | collections
    | INT DOT DOT INT"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ("range", p[1], p[4])


def p_while_block(p):
    "while_block : WHILE LPAREN expression RPAREN"
    p[0] = ("while_condition", p[3])


def p_while_statement(p):
    """while_statement : while_block LBRACE statements RBRACE
    | REPEAT LBRACE statements RBRACE while_block"""
    if len(p) == 5:
        p[0] = ("while", p[1], p[3])
    else:
        p[0] = ("repeat-while", ("repeat", p[3]), p[5])
