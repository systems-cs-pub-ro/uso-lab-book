#!/usr/bin/env python3

"""
Parse CSV file with USD exchange rate and print statistics.
"""

import sys
import csv


FILENAME = 'ECB_FX_USD-quote.csv'
CURRENCY = 'EUR'

# Data is read in list of tuples (pairs), i.e. (2020-02-21, 0.73).
# Date is the first item of the tuple / pair.
# Exchange rate is the next item in the tuple / pair.
data = []

# Store differential values in list of tuples (pairs), i.e. (2020-02-21, 0.012).
# This means that on 2020-02-21 there was an increase of 0.012 of the exchange rate
# compared to the previous day (2020-02-20).
diff_data = []


def print_highest_rate():
    sorted_data = list(sorted(data, key=lambda x: x[1]))
    print("Highest exchange rate: {} (on {})".format(sorted_data[-1][1], sorted_data[-1][0]))


def print_lowest_rate():
    sorted_data = list(sorted(data, key=lambda x: x[1]))
    print("Lowest exchange rate: {} (on {})".format(sorted_data[0][1], sorted_data[0][0]))


def print_largest_increase():
    sorted_data = list(sorted(diff_data, key=lambda x: x[1]))
    print("Largest increase of exchange rate: {} (on {})".format(sorted_data[-1][1], sorted_data[-1][0]))


def print_largest_decrease():
    sorted_data = list(sorted(diff_data, key=lambda x: x[1]))
    print("Largest decrease of exchange rate: {} (on {})".format(sorted_data[0][1], sorted_data[0][0]))


def print_largest_increase_period():
    largest_sequence_size = 0
    largest_sequence_start_date = diff_data[0][0]
    current_sequence_size = 0
    current_sequence_start_date = diff_data[0][0]
    for i in (range(len(diff_data)-1, 0, -1)):
        if diff_data[i][1] > 0:
            current_sequence_size += 1
        else:
            if current_sequence_size > largest_sequence_size:
                largest_sequence_size = current_sequence_size
                largest_sequence_start_date = current_sequence_start_date
            current_sequence_size = 0
            current_sequence_start_date = diff_data[i][0]

    print("Largest period of exchange rage increase: {} days starting from {}".format(largest_sequence_size, largest_sequence_start_date))


def print_largest_decrease_period():
    largest_sequence_size = 0
    largest_sequence_start_date = diff_data[0][0]
    current_sequence_size = 0
    current_sequence_start_date = diff_data[0][0]
    for i in (range(len(diff_data)-1, 0, -1)):
        if diff_data[i][1] < 0:
            current_sequence_size += 1
        else:
            if current_sequence_size > largest_sequence_size:
                largest_sequence_size = current_sequence_size
                largest_sequence_start_date = current_sequence_start_date
            current_sequence_size = 0
            current_sequence_start_date = diff_data[i][0]

    print("Largest period of exchange rage decrease: {} days starting from {}".format(largest_sequence_size, largest_sequence_start_date))


def main():

    with open(FILENAME, 'rt') as csvfile:
        reader = csv.reader(csvfile)
        # Read header.
        header = next(reader)
        date_idx = header.index('Date')
        currency_idx = header.index(CURRENCY)
        # Skip comment line.
        next(reader)
        # Read contents.
        for row in reader:
            data.append((row[date_idx], float(row[currency_idx])))

    # Compute differential data.
    for i in range(0, len(data)-1):
        cur_date = data[i][0]
        cur_value = data[i][1]
        prev_value = data[i+1][1]
        diff_data.append((cur_date, cur_value - prev_value))

    print_highest_rate()
    print_lowest_rate()
    print_largest_increase()
    print_largest_decrease()
    print_largest_increase_period()
    print_largest_decrease_period()


if __name__ == "__main__":
    sys.exit(main())
