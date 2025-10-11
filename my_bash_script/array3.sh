#!/bin/bash
clear
read -p "Enter the name by spacing to delete user: " -a values
for val in ${values[@]}
do
        sudo userdel -r $val
done
echo "${values[@]} deleted succesfully"

