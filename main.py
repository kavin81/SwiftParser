import argparse

from SwiftParser import parse

from rich import print
from rich.pretty import Pretty
from rich.panel import Panel


def main(file_path):
    with open(file_path, "r") as file:
        code = file.read()

    parsed_code = parse(code)
    print(
        Panel.fit(
            Pretty(parsed_code),
            title="Parsed Code",
        ),
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Parse Swift code from a file.")

    parser.add_argument(
        "--file",
        "-f",
        type=str,
        required=False,
        default="examples/main.swift",
        help="Path to the file containing the Swift code. (default: examples/main.swift)",
    )

    args = parser.parse_args()

    main(args.file)
