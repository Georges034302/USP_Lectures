#!/bin/bash

n=${1:-10} # this checks for the first argument

echo "Preview $n lines from cities.txt"
head -$n cities.txt

