#!/bin/bash

# Empty array declare
numbers=()

# Sum initialize
sum=0

echo "Enter numbers (press 'q' to stop):"

while true
do
    read -p "Enter number: " num
    if [[ $num == "q" ]]; then
        break
    fi
    # Array में जोड़ना
    numbers+=($num)
done

# Array elements का sum निकालना
for n in "${numbers[@]}"
do
    sum=$((sum + n))
done

echo "You entered: ${numbers[@]}"
echo "Sum = $sum"

