#!/bin/bash

PS3="Choice (A/B/C/X): "
select choice in A B C X
do
case "$choice" in
	A) echo "A is selected" ;;
	B) echo "B is selected" ;;
	C) echo "C is selected" ;;
	X) break ;;
	*) echo "Unknown choice" ;;
esac
done
