#!/bin/bash

# Read username and password from STDIN
# check if username is george
# check if password is admin

echo -n "Username: "
read user

read -s -p "Password: " pass


if [[ $user == "george" && $pass == "admin" ]]; then
	echo -e "\nWelcome $user"
else
	echo -e "\nIncorrect credentials"
fi
