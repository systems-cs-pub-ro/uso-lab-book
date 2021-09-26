#!/usr/bin/env python3

"""
Parse JSON log output from testssl.sh.
"""

import sys
import json
import logging


# Configure default logging level.
logging.basicConfig(level=logging.WARNING)

# Store JSON information as a dictionary variable (`data`).
data = {}


def print_grade():
    """Print grading information (`final_score` and `overall_grade`) in `data`
    dictionary.

    To get to the grading information, the `data` dictionary must be traversed
    as follows:
      * Extract the list data['scanResult']. The list has only one item.
      * Extract the single item of the list: data['scanResult'][0]. This is a dictionary.
      * Extract the 'rating' element in the new dictionary (a list).
      * This list is a list of dictionary items, with the keys: 'id',
        'finding'.
      * The 'id' can be 'final_score' or 'overall_grade'.
    """

    final_score = 'TODO'
    overall_grade = 'TODO'
    if 'scanResult' not in data.keys():
        return
    if 'rating' not in data['scanResult'][0].keys():
        return
    rating_list = data['scanResult'][0]['rating']
    logging.debug(rating_list)
    for item in rating_list:
        if item['id'] == 'final_score':
            final_score = item['finding']
        if item['id'] == 'overall_grade':
            overall_grade = item['finding']

    print("final_score: {}, overall_grade: {}".format(final_score, overall_grade))


def print_vulnerabilities():
    """Print vulnerability information in `data` dictionary.
    Print vulnerabilities whose severity is NOT `OK`.

    To get to the vulnerability information, the `data` dictionary must be traversed
    as follows:
      * Extract the list data['scanResult']. The list has only one item.
      * Extract the single item of the list: data['scanResult'][0]. This is a dictionary.
      * Extract the 'vulnerabilities' element in the new dictionary (a list).
      * This list is a list of dictionary items, with the keys: 'id',
        'cve', 'severity'.
      * The 'id' key of the item is the identifier of the vulnerability.
      * The 'severity' of the item may be `OK` or something else.
    """

    if 'scanResult' not in data.keys():
        return
    if 'vulnerabilities' not in data['scanResult'][0].keys():
        return
    vulnerabilities_list = data['scanResult'][0]['vulnerabilities']
    logging.debug(vulnerabilities_list)
    print("\nVulnerabilities:\n")
    for item in vulnerabilities_list:
        if item['severity'] != 'OK':
            print('{} ({}) - {}'.format(item['id'], item['cve'], item['severity']))


def main():
    """Load JSON log files and call other functions.
    """
    global data

    if len(sys.argv) != 2:
        print("Usage: {} <filename>".format(sys.argv[0]))
        sys.exit(1)

    fname = sys.argv[1]
    with open(fname, 'rt') as jsonfile:
        data = json.load(jsonfile)

    if 'scanResult' in data.keys():
        logging.debug(data['scanResult'][0].keys())

    print_grade()
    print_vulnerabilities()


if __name__ == "__main__":
    sys.exit(main())
