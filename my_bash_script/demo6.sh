#!/bin/bash
read -p "Enter your numbers with space on terminal: " -a numbers
echo "your Entered numbers are: ${numbers[@]}"
echo "Your first number is: ${numbers[0]}"
echo Number of arguments pass: ${#numbers[@]}
echo "Your last number is: ${numbers[-1]}"
sum=0
for n in "${numbers[@]}"; do
    ((sum+=n))
done

echo "Sum of numbers is: $sum"

