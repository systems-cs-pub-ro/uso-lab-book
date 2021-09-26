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
    echo "File $fname doesn't not exist." 1>&2
    exit 1
fi

# Ignore header and read contents.
IFS=','
< "$fname" tail -n +2 |\
    while read _rank _lang _rest; do
        if test "$_lang" = "$lang"; then
            echo "$_rank,$_lang,$_rest"
        fi
    done |\
        sort -t ',' -k 1n | head -10
