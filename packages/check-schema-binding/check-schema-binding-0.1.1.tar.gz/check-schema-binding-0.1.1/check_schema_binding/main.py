import argparse
import os
import re
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check")
    args = parser.parse_args()

    has_error = False
    pattern = re.compile(r'CREATE\s.*VIEW', re.IGNORECASE)
    binding_re = re.compile(r'WITH\s+NO\s+SCHEMA\s+BINDING', re.IGNORECASE)
    for filename in args.filenames:

        if not filename.endswith('.sql'):
            continue

        with open(filename, "r") as sql_file:
            content = sql_file.read()

        if pattern.findall(content):

            if not binding_re.findall(content):
                print(f"'WITH NO SCHEMA BINDING' is missing in: {filename}")
                has_error = True

    if has_error:
        sys.exit(1)


if __name__ == "__main__":
    main()
