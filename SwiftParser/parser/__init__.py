# ruff: noqa: E402, F403

import ply.yacc as yacc
from ..lexer.tokens import tokens
from pathlib import Path

try:
    from dotenv import get_key

    dotenv_path = Path(__file__).resolve().parents[2] / ".env"
    debug_flag = (get_key(dotenv_path, "PYTHON_ENV") or "PROD") == "DEV"
except ImportError:
    debug_flag = False

"""
imports:
    root: Root-level parsing rules.
    util: utils for parser/.
    types: type declarations parsing
    statements: Loop and selection statements parsing.
    funcs: func parsing
"""

# base
from .root import *
from .util import *
from .types import *

# statements
from .statements import *


parser = yacc.yacc(
    debug=debug_flag,
    outputdir="./build",
    optimize=True,
)

__all__ = [
    "parser",
    "tokens",
]
