#!/bin/bash

read -p "Enter the file name: " filename
if [[ -z "$filename" ]]; then
	echo "File name should not be blank"
elif [[ ! -e "$filename" ]]; then
	echo "File does not exist"
elif [[ -f "$filename" && -w "$filename" ]]; then
	echo "Writting process start"
	cat >> $filename
else
	echo "You do not have permission of write"
fi
