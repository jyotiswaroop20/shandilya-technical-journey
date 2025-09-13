#!/bin/bash

read -p "Enter your input to check weather it is directory or not: " file
if [[ -d $file ]]; then
    echo "$file is a directory."
else
    echo "$file is not a directory."
fi

