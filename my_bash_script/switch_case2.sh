#!/bin/bash
read -p "Enter the service to install: " service

case $service in 
	httpd)
		dnf install httpd -y
		sleep 3
		clear
		systemctl enable --now httpd
		sleep 3
		clear
		systemctl status httpd
		;;
	gcc)
		dnf install gcc -y
		sleep 3
		clear
		;;
	E)
		echo "Exiting... Goodbye!"
		exit 0
		;;
	*)
		echo "Invalid choice!"
		;;
esac
	

