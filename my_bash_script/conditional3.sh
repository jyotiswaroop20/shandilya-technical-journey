#!/bin/bash
read -p "Enter your file name: " filename
if [[ -a $filename ]]; then
	echo "$filename exist"
else
	echo "$filename does not exist"
fi
