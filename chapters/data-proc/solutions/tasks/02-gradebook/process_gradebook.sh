#!/bin/bash

#
# Process gradebook in CSV format.
#

if test $# -ne 1; then
    echo "Usage: $0 <file>" 1>&2
    exit 1
fi

fname="$1"

if test ! -f "$fname"; then
    echo "File $fname doesn't not exist." 1>&2
    exit 1
fi

function compute_average()
{
    col_idx="$1"
    sum=$(< "$fname" cut -d ',' -f "$col_idx" | grep -v 'absent' | grep -v '^$' | paste -d '+' -s | bc)
    num=$(< "$fname" cut -d ',' -f "$col_idx" | grep -v 'absent' | grep -v '^$' | wc -l)
    echo "scale=2; $sum / $num" | bc
}

# Sort grades by column 2 (counted from 0): 'Punctaj final'.
< "$fname" LANG=C sort -t ',' -k 3rg

# Compute average of columns.
echo "Average (Notă finală): $(compute_average 2)"
echo "Average (Punctaj final): $(compute_average 3)"
echo "Average (Notă curs): $(compute_average 4)"
echo "Average (Examen final): $(compute_average 5)"
echo "Average (Notă lucrări): $(compute_average 7)"
echo "Average (Notă teme): $(compute_average 25)"

# Compute number of elements in Notă finală with 10 or (4 or nothing).
num=$(< "$fname" cut -d ',' -f 2 | grep '^10$' | wc -l)
echo "Number of items (Notă finală) with value of 10: $num"
num=$(< "$fname" cut -d ',' -f 2 | grep '^\(4\|\|absent\|abs\)$' | wc -l)
echo "Number of items (Notă finală) with value of 4 or nothing: $num"
