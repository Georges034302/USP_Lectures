#!/bin/bash

echo -n "City: "
read city

if [ $city = "Canberra" ]
then
	echo "This is the captial"
else
	echo "This is another city"
fi

echo "Goodbye"
