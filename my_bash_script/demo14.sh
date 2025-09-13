#!/bin/bash
read -p "Enter your first string: " string1
read -p "Enter your second string: " string2

if [[ "$string1" > "$string2" ]]; then
    echo "$string1 is greater than $string2!"
elif [[ "$string1" < "$string2" ]]; then
    echo "$string1 is less than $string2!"
else
    echo "Both strings are equal!"
fi


