#!/bin/bash
read -p "Enter your file address: " file
if [[ -a $file ]]; then
    echo "$file exists."
    
else
    echo "$file does not exist."
fi
