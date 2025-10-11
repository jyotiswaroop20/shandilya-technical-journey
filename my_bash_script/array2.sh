#!/bin/bash
clear
read -p "Enter the name by spacing to add user: " -a values
for val in ${values[@]}
do
	sudo useradd -m $val
done
echo "${values[@]} added succesfully"

