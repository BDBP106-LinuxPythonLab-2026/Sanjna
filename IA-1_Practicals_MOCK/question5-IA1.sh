#!/bin/bash

if [ "$#" -eq 4 ]
then
	echo "Argument 1 is: $1"
	echo "Argument 2 is: $2"
	echo "Argument 3 is: $3"
	echo "Argument 4 is: $4"
else
	exit 200
fi
