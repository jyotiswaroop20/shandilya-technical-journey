#!/bin/bash
read -p "Enter Your Value in Array by spacing: " -a value
echo "The first value ${value[0]}"
echo "The second value ${value[1]}"
echo "The third value ${value[2]}"
echo "The last value of array ${value[-1]}"
echo "All values of array ${value[@]}"
