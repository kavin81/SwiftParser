from .lexer import lexer
from .parser import parser


def parse(code):
    lexer.input(code)
    tokens = []

    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)

    try:
        from rich.console import Console
        from rich.panel import Panel
        from rich.pretty import Pretty

        console = Console()
        console.print(Panel.fit(Pretty(tokens), title="Parsed Tokens"))
    except ImportError:
        print("Parsed Tokens:\n", tokens)

    return parser.parse(code)
