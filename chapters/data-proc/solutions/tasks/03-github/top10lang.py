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

    data = []
    with open(fname, 'rt') as csvfile:
        csvreader = csv.reader(csvfile)
        # Skip header.
        next(csvreader)
        for row in csvreader:
            if row[1] == lang:
                data.append(row)

    for mytuple in sorted(data, key=lambda x: int(x[0]))[0:10]:
        print(','.join(item for item in mytuple))


if __name__ == "__main__":
    sys.exit(main())
