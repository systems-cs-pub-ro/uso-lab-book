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
    echo "File $fname doesn't exist." 1>&2
    exit 1
fi

function compute_average()
{
    col_idx="$1"
    # TODO: This is just a placeholder. Remove this.
    sum=10
    num=2
    # TODO: Extract sum and number of items in column 'col_idx'.

    echo "scale=2; $sum / $num" | bc
}

# TODO: Sort grades by column 2 (counted from 0): 'Punctaj final'.

# Compute average of columns.
echo "Average (Notă finală): $(compute_average 2)"
echo "Average (Punctaj final): $(compute_average 3)"
echo "Average (Notă curs): $(compute_average 4)"
echo "Average (Examen final): $(compute_average 5)"
echo "Average (Notă lucrări): $(compute_average 7)"
echo "Average (Notă teme): $(compute_average 25)"

# Compute number of elements in Notă finală with 10 or (4 or nothing).
# TODO: This is just a placeholder. Remove this.
num=1
# TODO: Compute number of elements equal to 10.

echo "Number of items (Notă finală) with value of 10: $num"

# TODO: Compute number of elements equal to 4 or empty or 'absent'.
echo "Number of items (Notă finală) with value of 4 or nothing: $num"
