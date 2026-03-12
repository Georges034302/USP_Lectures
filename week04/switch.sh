#!/bin/bash

select choice in A B X
do
  case "$choice" in
    A) echo "A is selected" ;;
    B) echo "B is selected" ;;
    X) break ;;
    *) echo "Undefined" ;;
  esac
done
