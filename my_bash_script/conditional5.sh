#!/bin/bash

while true; do
    read -p "Enter your username: " username
    read -sp "Enter your password: " password
    echo

    if [[ -z "$username" || -z "$password" ]]; then
        echo "Username and Password should not be blank"
        continue   # loop फिर से चलेगा, दोबारा input लेगा
    elif [[ "$username" == "atripathi" && "$password" == "Software123@" ]]; then
        echo "Welcome! $username"
        sleep 2
        clear
	
        echo "The below menu displays the task you can perform"
        echo "A - Add user"
        echo "D - Delete user"
        echo "Q - Quit"
        read -p "Enter your choice: " choice

        if [[ -z "$choice" ]]; then
            echo "Choice should not be blank"
            continue   # फिर से menu दिखेगा
        else
            case $choice in
                A)
                    read -p "Enter names (space-separated) to add users: " -a names
                    for name in "${names[@]}"; do
                        sudo useradd -m -c "$name" "$name"
                        echo "User $name added"
                    done
		    echo
		    echo "Now you can see added user details below in passwd file....."
		    echo
		    cat /etc/passwd | tail
		    echo
		    break
                    ;;
                D)
                    read -p "Enter names (space-separated) to delete users: " -a names
                    for name in "${names[@]}"; do
                        sudo userdel -r "$name"
                        echo "User $name deleted"
                    done
		    echo
                    echo "Now you can see deleted user details below in passwd file....."
		    echo
		    cat /etc/passwd | tail
		    echo
		    break
                    ;;
                Q)
                    echo "Exiting..."
                    break   # पूरा loop खत्म कर देगा
                    ;;
                *)
                    echo "Invalid option"
                    ;;
            esac
        fi
    else
        echo "Invalid username or password"
        continue   # फिर से दोबारा input लेगा
    fi
done

