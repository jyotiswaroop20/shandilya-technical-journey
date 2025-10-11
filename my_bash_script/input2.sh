#!/bin/bash
clear
read -p "Enter the username: " username
read -p "Enter the shellname in the form of /bin/shell_name: " shell

if getent passwd "$username" >/dev/null; then
    sudo usermod -s "$shell" "$username" 
    echo "Shell changed for $username"
else
    echo "User $username does not exist"
fi

