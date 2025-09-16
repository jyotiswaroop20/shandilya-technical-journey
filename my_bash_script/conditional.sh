#!/bin/bash
read -p "Enter your numer: " num
if [ $((num%2)) -eq 0 ]; then
	mkdir test1
else
	mkdir test2
fi
