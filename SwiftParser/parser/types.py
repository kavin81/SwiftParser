def p_bin_operators(p):
    """bin_operators : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | MOD
    | EQEQ
    | NOT_EQUAL
    | LESS
    | LESS_EQUAL
    | GREATER
    | GREATER_EQUAL
    | AND
    | OR"""
    p[0] = p[1]


### TYPE HINTS ###


def p_basic_typehints(p):
    """basic_typehints : INT_TYPE
    | FLOAT_TYPE
    | BOOL_TYPE
    | STRING_TYPE
    | SET_TYPE"""
    p[0] = p[1]


def p_typehint(p):
    """typehint : LBRACKET basic_typehints RBRACKET
    | LBRACKET basic_typehints COLON basic_typehints RBRACKET
    | basic_typehints"""
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 6:
        p[0] = (p[2], p[4])
    else:
        p[0] = p[1]


### VALUE  ASSIGNED ###


def p_basic_types(p):
    """basic_types : INT
    | FLOAT
    | BOOL
    | STRING
    | collections"""
    p[0] = p[1]


### generic collections ###

# collections => [collection_contents] || (collection_contents)
# collection_contents => collection_content , collection_contents | collection_content
# collection_content => basic_types | basic_types : basic_types


def p_collections(p):
    """collections : LBRACKET collection_contents RBRACKET
    | LPAREN collection_contents RPAREN"""
    p[0] = p[2]


def p_collection_contents(p):
    """collection_contents : collection_content
    | collection_content COMMA collection_contents"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_collection_content(p):
    """collection_content : basic_types
    | basic_types COLON basic_types"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])
