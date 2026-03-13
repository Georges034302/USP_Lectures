#!/bin/bash

# Add positive even numbers from STDIN until -1

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

echo "Even Sum = $sum"
