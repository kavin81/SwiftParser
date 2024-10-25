def p_if_statement(p):
    """if_statement : IF LPAREN expression RPAREN LBRACE statements RBRACE elifs else_statement"""
    p[0] = ("if", p[3], p[6], p[8], p[9])


def p_elifs(p) -> None:
    """elifs : elifs ELIF LPAREN expression RPAREN LBRACE statements RBRACE
    | empty"""
    if len(p) == 9:
        p[0] = ("elif", p[4], p[7], p[1])
    else:
        p[0] = ("elif", None)


def p_else_statement(p):
    """else_statement : ELSE LBRACE statements RBRACE
    | empty"""
    if len(p) == 5:
        p[0] = ("else", p[3])
    else:
        p[0] = ("else", None)
