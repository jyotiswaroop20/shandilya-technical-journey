#!/bin/bash
count=1

until [ $count -gt 10 ]; do
    if [[ $count == 3 ]]; then
        ((count++))
        continue
    fi
    echo $count
    ((count++))
done

