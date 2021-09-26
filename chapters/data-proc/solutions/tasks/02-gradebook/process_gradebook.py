#!/usr/bin/env python3

"""
Process gradebook in CSV format.
"""

import sys
import csv
import logging


# Configure default logging level.
logging.basicConfig(level=logging.WARNING)

# Store grading information in a list variable (`data`).
# This is a list of tuples.
data = []


def sort_by_column(col_idx):
    """Sort grades by column.
    Column is float but 'data' is a list of tuples of strings.
    We convert the tuple elemnt to float when sorting.
    """
    sorted_data = sorted(data, key=lambda x: float(x[col_idx]), reverse=True)
    for item in sorted_data:
        print(",".join(i for i in item))


def compute_average(col_idx):
    """Compute average of column and print message.
    Column is float but 'data' is a list of tuples of strings.
    We convert the tuple elemnt to float when computing average.
    We ignore empty elements.
    """
    column = [float(item[col_idx]) for item in data if item[col_idx] != '' and item[col_idx] != 'absent']
    return sum(column)/len(column)


def compute_num_values(col_idx, value):
    """Compute number of elements in column 'col_idx' equal to 'value'.
    """
    return len([item for item in data if item[col_idx] == value])


def main():
    global data

    if len(sys.argv) != 2:
        print("Usage: {} <gradebook.csv>".format(sys.argv[0], file=sys.stderr))
        sys.exit(1)

    fname = sys.argv[1]

    # List variable to collect rows.
    data = []
    with open(fname, 'rt') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(tuple(row))

    sort_by_column(2)

    avg = compute_average(1)
    print("Average ({}): {:.2f}".format('Notă finală', avg))
    avg = compute_average(2)
    print("Average ({}): {:.2f}".format('Punctaj final', avg))
    avg = compute_average(3)
    print("Average ({}): {:.2f}".format('Notă curs', avg))
    avg = compute_average(4)
    print("Average ({}): {:.2f}".format('Examen final', avg))
    avg = compute_average(6)
    print("Average ({}): {:.2f}".format('Notă lucrări', avg))
    avg = compute_average(24)
    print("Average ({}): {:.2f}".format('Notă teme', avg))

    num = compute_num_values(1, '10')
    print("Number of items (Notă finală) with value of 10: {}".format(num))
    num = compute_num_values(1, '4')
    num += compute_num_values(1, '')
    num += compute_num_values(1, 'absent')
    print("Number of items (Notă finală) with value of 4 or nothing: {}".format(num))


if __name__ == "__main__":
    sys.exit(main())
