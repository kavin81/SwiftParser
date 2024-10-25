"""
__author__ = "Kavin S, M V Chinmay"

"""

from SwiftParser import parse


from rich import print
from rich.pretty import Pretty
from rich.panel import Panel


def main():

    basic_types = """
    let a : [Int : Float] = [10,10]
    let b : Int = 10
    a = "Hello"
    """

    selection_statement = """
    if (a > b) {
        a = 1
    } else {
        a = 2
    }
    """

    loop_statement = """
    for i in 10..100 {
        a = a + 1
    }
    while (a < 10) {
        a = a + 1
    }

    repeat {
        a = a + 1
    } while (a < 10)

    """

    code = basic_types + selection_statement + loop_statement

    parsed_code = parse(code)
    print(
        Panel.fit(
            Pretty(parsed_code),
            title="Parsed Code",
        ),
    )


if __name__ == "__main__":
    main()
