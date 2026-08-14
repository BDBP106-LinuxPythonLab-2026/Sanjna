#!/bin/bash

echo -n "Enter a file name"
read filename

if [ -f "$filename" ]; then
	if [ -x "$filename" ]; then
		echo "File exists and is executable"
	else 
		echo "File exists but is not executable"
		exit 200
	fi
else
	echo "File does not exist"
	exit 201
fi

