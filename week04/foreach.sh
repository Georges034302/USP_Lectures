#!/bin/bash

# Show unique sorted file from argument

for line in $(cat $1)
do
	echo $line
done | sort | tr 'A-Z' 'a-z' | uniq
