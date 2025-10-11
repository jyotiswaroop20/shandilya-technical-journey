#!/bin/bash

for username in $(cut -d: -f1,7 /etc/passwd)
do
	echo "User & Default Login Shell: $username"
done
