#!/bin/bash

read -p "Mode (h/t): " mode

read -p "How Many lines: " n

[ "$mode" = "h" ] && head -n "$n" cities.txt
[ "$mode" = "t" ] && tail -n "$n" cities.txt
