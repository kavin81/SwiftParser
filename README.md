# SwiftParser

## Description
a mini project to validate some basic structures of Swift built using PLY


## features/structures

- [x] simple data type declaration
  - [x] integer
  - [x] float
  - [x] string
  - [x] boolean

- [x] array-like data types
  - [x] list
  - [x] tuple
  - [x] set
  - [x] dictionary


- [x] selection statements
  - [x] if
    - [x] else
    - [x] elif

- [x] loop statements
  - [x] for
  - [x] while

- [x] functions declaration
  - [x] with parameters
  - [x] without parameters
  - [x] with return type
  - [x] without return type

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/kavin81/SwiftParser
    ```
2. Navigate to the project directory:
    ```bash
    cd SwiftParser
    ```
3. Install dependencies:
    ```bash
    # using pip
    pip install -r requirements.txt
    ```
    ```
    # using conda/mamba
    conda env create -f environment.yml
    ```


## Usage

```bash
>> python main.py --help

usage: script_name.py [-h] [--file FILE | -f FILE]

Parse Swift code from a file.

optional arguments:
    -h, --help            show this help message and exit
    --file FILE, -f FILE  Path to the file containing the Swift code. (default: examples/main.swift)
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
