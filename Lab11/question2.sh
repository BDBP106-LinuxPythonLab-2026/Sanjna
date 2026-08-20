#!/bin/bash

#Difference between -e -f and -s in the if block

# -e operator checks if a file exists
# -f operator checks if the file is a regular file or not

if [ -e "newdir" ]; then
		if [ -f "Documents" ]; then
			echo "The file exists and is a regular file"
		else 
			echo "The file exists but is not a regular file"
		fi
else
       echo "The file does not exist"	
	
fi

#The output is that the file exists but is not a regular file since it is a directory

# -s operator checks if a file is non-empty

if [ -s "empty_file" ]; then
	echo "The file is not empty"
else
	echo "The file is empty"
fi

#The output is "The file is empty"
