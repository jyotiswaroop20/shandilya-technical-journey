#!/bin/bash

echo "============================="
echo "   Simple Menu Using case    "
echo "============================="
echo "1. Show Date"
echo "2. Show Current Directory"
echo "3. Show Logged-in Users"
echo "4. Exit"
echo -n "Enter your choice [1-4]: "
read choice

case $choice in
    1)
        echo "Today's Date and Time:"
        date
        ;;
    2)
        echo "Current Directory:"
        pwd
        ;;
    3)
        echo "Currently Logged-in Users:"
        who
        ;;
    4)
        echo "Exiting... Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid choice! Please enter between 1 to 4."
        ;;
esac

