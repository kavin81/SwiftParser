token_categories = {
    "parentheses": ["LPAREN", "RPAREN"],
    "braces": ["LBRACE", "RBRACE"],
    "brackets": ["LBRACKET", "RBRACKET"],
    "punctuations": ["COMMA", "COLON", "SEMICOLON", "DOT"],
    "operators": ["PLUS", "MINUS", "TIMES", "DIVIDE", "MOD"],
    "assignment": ["LET", "VAR", "EQUAL"],
    "types": ["INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE", "STRING_TYPE", "SET_TYPE"],
    "selection_statements": ["IF", "ELSE", "ELIF"],
    "loop_statements": ["FOR", "WHILE", "REPEAT", "IN"],
    "comparison_operators": [
        "EQEQ",
        "NOT_EQUAL",
        "LESS",
        "LESS_EQUAL",
        "GREATER",
        "GREATER_EQUAL",
    ],
    "logical_operators": ["NOT", "AND", "OR"],
    "literals": ["IDENTIFIER", "FLOAT", "INT", "BOOL", "STRING"],
}

tokens = tuple(token for category in token_categories.values() for token in category)

reserved = {
    "let": "LET",
    "var": "VAR",
    "Int": "INT_TYPE",
    "Float": "FLOAT_TYPE",
    "Set": "SET_TYPE",
    "Bool": "BOOL_TYPE",
    "String": "STRING_TYPE",
    "if": "IF",
    "else": "ELSE",
    "elif": "ELIF",
    "for": "FOR",
    "while": "WHILE",
    "repeat": "REPEAT",
    "in": "IN",
    "true": "BOOL",
    "false": "BOOL",
}
