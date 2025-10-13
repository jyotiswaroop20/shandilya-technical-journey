#!/bin/bash
if (( $EUID == 0 )); then
	echo "You are a $USER user"
else
	echo "you are not a root user"

fi
