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
    for (syscall_id, syscall_name, status) in syscall_status:
        found = False
        for (syscall_name_2, num_apps) in syscall_use:
            if syscall_name == syscall_name_2:
                found = True
                data.append((syscall_id, syscall_name, status, num_apps))
        if not found:
            data.append((syscall_id, syscall_name, status, 0))


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
    sorted_data = sorted([item for item in data if item[2] != 'okay'], key=lambda x: x[3], reverse=True)
    for (syscall_id, syscall_name, status, num_apps) in sorted_data[0:top_num]:
        print("{},{},{},{}".format(syscall_id, syscall_name, status, num_apps))


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
