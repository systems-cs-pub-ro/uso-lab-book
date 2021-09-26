#!/bin/bash

#
# Extract top 10 repositories by programming language from GitHub ranking.
#

if test $# -ne 2; then
    echo "Usage: $0 <file> <language>" 1>&2
    exit 1
fi

fname="$1"
lang="$2"

if test ! -f "$fname"; then
    echo "File $fname doesn't exist." 1>&2
    exit 1
fi

# Ignore header and read contents.
IFS=','
< "$fname" tail -n +2 # | ...

# TODO Select lines with language (2nd column) equal to `lang` variable.

# TODO: Print first 10 items in selection.
