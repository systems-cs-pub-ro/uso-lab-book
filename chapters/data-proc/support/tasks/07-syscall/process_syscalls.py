#!/usr/bin/env python3

"""
Process Unikraft system call status files.
"""

import sys
import csv
import logging


SYSCALL_STATUS_FILENAME = "syscall-status.csv"
SYSCALL_USE_FILENAME = "syscall-use.csv"

# Configure default logging level.
logging.basicConfig(level=logging.WARNING)

# Store system call information in a list variable (`data`).
# This is a list of tuples.
# A tuple is (syscall_id, syscall_name, status, num_apps).
data = []


def unify(syscall_status, syscall_use):
    """Unify CSV-style information in syscall_status and syscall_use lists.
    Result si aggregated in 'data' list variable.
    """
    # TODO: Traverse syscall_status and syscall_use and add items in data.
    # Join by syscall_name in both lists.
    # Use constructs such as:
    #   for (syscall_id, syscall_name, status) in syscall_status
    #   for (syscall_name_2, num_apps) in syscall_use


def print_all():
    """Print all contents of 'data' list variable.
    """
    print("syscall_id,syscall_name,status,num_apps")
    for (syscall_id, syscall_name, status, num_apps) in data:
        print("{},{},{},{}".format(syscall_id, syscall_name, status, num_apps))


def print_top_not_okay(top_num):
    """Print top_num contents of 'data' list variable sorted by num_apps
    for those system calls whoe status is NOT 'okay'.
    """
    print("")
    # TODO: Select first 'top_num' items in data not 'okay' sorted them by 'num_apps'.


def main():
    """Load syscall CSV files and call processing functions.
    """
    global data

    syscall_status = []
    with open(SYSCALL_STATUS_FILENAME, 'rt') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            syscall_status.append((int(row[0]), row[1], row[2]))

    syscall_use = []
    with open(SYSCALL_USE_FILENAME, 'rt') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            syscall_use.append((row[0], int(row[1])))

    unify(syscall_status, syscall_use)
    print_all()
    print_top_not_okay(10)


if __name__ == "__main__":
    sys.exit(main())
