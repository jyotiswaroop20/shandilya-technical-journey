#!/bin/bash
read -p "Enter your input in array by spacing: " -a users
for user in ${users[@]}
do
echo "$user"
done
