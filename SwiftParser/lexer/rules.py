import ply.lex as lex
from .tokens import tokens, reserved

# paranthesis
t_LPAREN = r"\("
t_RPAREN = r"\)"
# braces
t_LBRACE = r"\{"
t_RBRACE = r"\}"
# brackets
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
# punctuations
t_COMMA = r","
t_COLON = r":"
t_SEMICOLON = r";"
t_DOT = r"\."
# operators
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_MOD = r"%"
# assignment
t_LET = r"let"
t_VAR = r"var"
t_EQUAL = r"="
# types
t_INT_TYPE = r"Int"
t_FLOAT_TYPE = r"Float"
t_BOOL_TYPE = r"Bool"
t_STRING_TYPE = r"String"
t_SET_TYPE = r"Set"

# selection statements
t_IF = r"if"
t_ELSE = r"else"
t_ELIF = r"elif"

# loop statements
t_FOR = r"for"
t_WHILE = r"while"
t_REPEAT = r"repeat"
t_IN = r"in"


# comparison operators
t_EQEQ = r"=="
t_NOT_EQUAL = r"!="
t_LESS = r"<"
t_LESS_EQUAL = r"<="
t_GREATER = r">"
t_GREATER_EQUAL = r">="
# logical operators
t_NOT = r"!"
t_AND = r"&&"
t_OR = r"\|\|"


def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "IDENTIFIER")
    return t


def t_FLOAT(t):
    r"[-+]?\d+\.\d+"
    t.value = float(t.value)
    return t


def t_INT(t):
    r"[-+]?\d+"
    t.value = int(t.value)
    return t


def t_BOOL(t):
    r"(true|false)"
    t.value = True if t.value == "true" else False
    return t


def t_STRING(t):
    r"\"(.*?)\"|\'(.*?)\'"
    t.value = str(t.value[1:-1])
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = " \t"


def t_error(t):
    print(
        f"Syntax error at line {t.lineno}, position {t.lexpos}, token {t.type}, value {t.value}"
    )
    t.lexer.skip(1)
