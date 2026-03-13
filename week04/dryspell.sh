#!/bin/bash

# Read rain until -1.
# Show the longest dry spell
# Dry spell is the number of days with zero rain


read -p "rain: " rain
count=0
max=0
while [ $rain -ne -1 ]
do
	if [ $rain -eq 0 ]
	then
		((count++))
	else
		if [ $max -lt $count ]
		then
			max=$count
		fi
		count=0
	fi
	read -p "rain: " rain
done
if [ $max -lt $count ]
then
	max=$count
fi
echo "Longest dry spell = $max"
