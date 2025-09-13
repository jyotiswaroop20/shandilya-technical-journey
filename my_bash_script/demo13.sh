#!/bin/bash
read -p "Enter your first string: " string1
read -p "Enter your second string: " string2

if [[ ${string1} == ${string2} ]]; then
    echo "Both strings are equal!"
else
    echo "Strings are not equal!"
fi

