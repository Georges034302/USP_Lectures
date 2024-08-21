#!/bin/bash

# Read a string from STDIN
# Check if the string is a file or a directory
# if the string does not exist offer the user the options:
# d - create a directory
# f - to create a file

# echo -n "String: "
# read s
read -p "String: " s

if [ -f $s ]
then
	echo "$s is a file"
elif [ -d $s ]
then
	echo "$s is a directory"
else
	echo "$s does not exist"
	read -p "Create (f/d): " choice
	if [ "$choice" == "f" ]
	then
		touch $s
	elif [ "$choice" == "d" ]
	then
		mkdir $s
	else
		echo "Incorrect command"
	fi
fi

