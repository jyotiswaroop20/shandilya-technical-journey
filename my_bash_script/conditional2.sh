#!/bin/bash
echo "*****Select Your Choice*****"
echo "To install httpd enter:H"
echo "To install zsh enter:Z"
read -p "Enter your choice: " choice
if [[ $choice == "H" ]]; then
	dnf install httpd -y
	systemctl start httpd
	systemctl enable --now httpd
	systemctl status httpd
elif [[ $choice == "Z" ]]; then
	dnf install zsh -y
else
	echo "Invalid Choice"
fi
