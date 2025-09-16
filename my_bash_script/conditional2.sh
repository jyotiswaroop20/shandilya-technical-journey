#!/bin/bash
echo "*****Select Your Choice*****"
echo "To install httpd enter:H"
echo "To install zsh enter:Z"
read -p "Enter your choice: " choice
if [[ $choice == "H" ]]; then
	dnf install httpd -y
	systemctl start httpd
	systemctl enable --now httpd
	clear
	sleep 2
	systemctl status httpd
elif [[ $choice == "Z" ]]; then
	dnf install zsh -y
	clear
	sleep 2
	rpm -qa | grep zsh
else
	echo "Invalid Choice"
fi
