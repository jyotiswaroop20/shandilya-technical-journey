#!/bin/bash
read -p "Enter your file name: " filename
if [[ -d $filename ]]; then
        echo "$filename exist and it is a directory"
else
        echo "$filename exist but it is not directory file"
fi

