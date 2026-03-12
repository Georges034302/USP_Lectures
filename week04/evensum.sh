#!/bin/bash

# Read positive integers until -1, add all even numbers
# Show the total

read -p "n = " n
sum=0

while [ $n -ne -1 ]
do
	if [ $(($n%2)) -eq 0 ]
	then
		sum=$(($sum+$n))
	fi
	read -p "n = " n
done

echo "Even sum = $sum"
