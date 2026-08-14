#!/bin/bash

echo -n 
"Enter a number"
read number

if [ $number -gt 0 ]; then
	echo "The number is a positive number"

elif [ $number -lt 0 ]; then
	echo "The number is a negative number"
else 
	echo "The number is zero"
fi	
