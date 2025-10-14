#!/bin/bash

users=$(cut -d: -f1 /etc/passwd)

for user in ${users}
do
	echo "USER'S NAME: ${user}"
done
