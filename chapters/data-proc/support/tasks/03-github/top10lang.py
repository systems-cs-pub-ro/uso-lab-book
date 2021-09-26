#!/usr/bin/env python3

"""
Extract top 10 repositories by programming language from GitHub ranking.
"""

import sys
import csv


def main():
    if len(sys.argv) != 3:
        print("Usage: {} <file> <language>".format(sys.argv[0], file=sys.stderr))
        sys.exit(1)

    fname = sys.argv[1]
    lang = sys.argv[2]

    # List variable to collect rows.
    data = []
    with open(fname, 'rt') as csvfile:
        csvreader = csv.reader(csvfile)
        # Skip header.
        next(csvreader)
        # TODO: Collect in `data` list variable lines with language (2nd column)
        # equal to `lang` variable.

    # TODO: Print first 10 items in `data` list variable.


if __name__ == "__main__":
    sys.exit(main())
