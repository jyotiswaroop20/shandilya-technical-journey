#!/bin/bash
read -p "Enter your name: " name

if [[ -z $name ]]; then
    echo "You didn't enter anything!"
else
    echo "Hello, $name!"
fi

