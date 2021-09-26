#!/usr/bin/env python

"""
Print lines in file in reverse.
"""

import sys
import os


def usage(argv0):
    print("Usage: {} <file>".format(argv0), file=sys.stderr)


def main():
    if len(sys.argv) != 2:
        usage(sys.argv[0])
        sys.exit(1)

    fname = sys.argv[1]
    if not os.path.isfile(fname):
        print("Argument {} is not a file.".format(fname), file=sys.stderr)
        sys.exit(1)

    with open(fname) as f:
        lines = f.readlines()[::-1]
        for l in lines:
            print(l.rstrip())


if __name__ == "__main__":
    main()
