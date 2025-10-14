#!/bin/bash

read -p "Enter your name? " name

while [[ -z ${name} ]]
do
	echo "Your name can not be blank. Please enter a valid name!"
	read -p "Enter your name? " name
done

echo "Hi there ${name}"
