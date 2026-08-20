#!/bin/bash

#To check if a string is empty or not


string1="String"
string2=""
# -z returns TRUE if the string is empty

if [ -z "$string1" ]; then

	echo "The string1 is empty"
else
	echo "The string1 is non-empty"
fi

# -n returns TRUE if the string is non-empty

if [ -n "$string2" ]; then
	echo "The string2 is non-empty"
else
	echo "The string2 is empty"
fi



