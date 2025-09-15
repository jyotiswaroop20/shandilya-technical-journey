#!/bin/bash
echo "This script is for searching file"
read -p "Enter your file name: " filename
if [[ -z "$filename" ]]; then
	echo "Error: File name cannot be empty!"
   	exit 1
else
	echo "Searching for file: $filename ..."
	file=`sudo find / -type f -name "$filename" 2>/dev/null`
	if [[ -z "$file" ]]; then
		echo "File does not exist"
	else
		echo $file
	fi
fi
