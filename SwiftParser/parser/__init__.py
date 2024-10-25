import ply.yacc as yacc
from ..lexer.tokens import tokens


from .util import *
from .root import *
from .types import *
from .statements import *


parser = yacc.yacc(
    debug=True,
    outputdir="./build",
    optimize=True,
)
