#!/bin/bash

read -p "Enter the file name:" f_name
if [[ -a ${f_name} ]]; then
	echo "File found"
else
	echo "File not found"
fi
