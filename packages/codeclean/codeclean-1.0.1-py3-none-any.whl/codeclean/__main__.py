"""
codeclean

Remove comments and docstrings from Python code.
"""
from re import sub, DOTALL
from os.path import isfile
from argparse import ArgumentParser


def remove_comments(code):
    """
    Removes comments from the code.
    """
    lines_list = []
    lines = code.split("\n")
    for line in lines:
        line = sub(r"\s*#.*$", "", line)
        lines_list.append(line)
    return "\n".join(lines_list)


def remove_docstrings(code):
    """
    Removes docstrings from the code.
    """
    code = sub(r'(?<!\\)"""[^"]*"""', "", code, flags=DOTALL)
    code = sub(r"(?<!\\)'''[^']*'''", "", code, flags=DOTALL)
    return code


def main():
    parser = ArgumentParser(
        description="Remove comments and docstrings from Python files."
    )
    parser.add_argument(
        "files", metavar="file", type=str, nargs="+", help="File(s) to process."
    )
    parser.add_argument("--comments", action="store_true", help="Remove comments.")
    parser.add_argument("--docstrings", action="store_true", help="Remove docstrings.")

    args = parser.parse_args()

    if not args.comments and not args.docstrings:
        print("Error: You must provide either the --comments or --docstrings flag.")
        return

    modified_code = {}

    for file in args.files:
        if not isfile(file):
            print(f"Error: '{file}' is not a valid file.")
            continue

        try:
            with open(file, "r", encoding="utf-8") as f:
                code = f.read()
        except IOError as e:
            print(f"Error while processing file '{file}': {str(e)}")
            continue

        if args.comments:
            code = remove_comments(code)

        if args.docstrings:
            code = remove_docstrings(code)

        modified_code[file] = code

    for file, code in modified_code.items():
        try:
            with open(file, "w", encoding="utf-8") as f:
                f.write(code)
                print(f"File '{file}' has been processed and modified.")
        except IOError as e:
            print(f"Error while writing to file '{file}': {str(e)}")


if __name__ == "__main__":
    main()
