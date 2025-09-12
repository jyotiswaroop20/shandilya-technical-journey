#!/bin/bash
echo "This script is for checking even odd"
read -p "Enter the number: " number
if [ $((number % 2)) -eq 0 ]; then
	echo "$number is even"
else
	echo "$number is odd"
fi
