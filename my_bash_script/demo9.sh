#!/bin/bash
read -p "Enter your file address: " file
if [[ -b $file ]]; then
    echo "$file exists."

else
    echo "$file does not exist."
fi

