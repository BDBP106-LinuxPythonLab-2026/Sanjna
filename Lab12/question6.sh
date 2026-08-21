#!/bin/bash

echo "Enter two numbers"
read n1 n2
function maximum {
	val1=$n1
	val2=$n2
	if [ "$val1" -gt "$val2" ]; then
		echo "The maximum is $val1"
	else
		echo "The maximum is $val2"
	fi
}
 
maximum $n1 $n2
