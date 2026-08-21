#!/bin/bash

#To print numbers from 0 to 10
n=0
while [ "$n" -lt 11 ]
do
	echo $n
	n=$[n+1]
done
