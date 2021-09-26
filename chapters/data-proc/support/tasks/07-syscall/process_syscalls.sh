#!/bin/bash

# Process Unikraft system call status files.

SYSCALL_STATUS_FILENAME="syscall-status.csv"
SYSCALL_USE_FILENAME="syscall-use.csv"

IFS=','
while read syscall_id syscall_name syscall_status; do
    line=$(grep "^$syscall_name," < "$SYSCALL_USE_FILENAME")
    if test $? -eq 0; then
        num_apps=${line##*,}
    else
        num_apps=0
    fi
    echo "$syscall_id,$syscall_name,$syscall_status,$num_apps"
done < <(<"$SYSCALL_STATUS_FILENAME" tail -n +2)

echo ""
while read syscall_id syscall_name syscall_status; do
    line=$(grep "^$syscall_name," < "$SYSCALL_USE_FILENAME")
    if test $? -eq 0; then
        num_apps=${line##*,}
    else
        num_apps=0
    fi
    if test "$syscall_status" != "okay"; then
        echo "$syscall_id,$syscall_name,$syscall_status,$num_apps"
    fi
done < <(<"$SYSCALL_STATUS_FILENAME" tail -n +2) | sort -t ',' -k 4rn | head -10
