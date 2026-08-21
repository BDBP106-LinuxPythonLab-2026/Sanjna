#!/bin/bash

function directory {
	dirname=$dir
	if [ -d "$dirname" ]; then
		echo $(ls $dirname)
	else
		mkdir "$dirname"
	fi
}

echo "Enter a directory name"
read dir
output=$(directory $dir)
echo "$output"
