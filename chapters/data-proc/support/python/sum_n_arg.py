#!/usr/bin/env python

import sys


def usage(argv0):
    print("Usage: {} <num>".format(argv0), file=sys.stderr)


def main():
    if len(sys.argv) != 2:
        usage(sys.argv[0])
        sys.exit(1)

    sum = 0
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Argument is not an integer.", file=sys.stderr)
        sys.exit(1)

    for i in range(1, n+1):
        sum += i

    print("sum(1,{}): {}".format(n, sum))


if __name__ == "__main__":
    main()
