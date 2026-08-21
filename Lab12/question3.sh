#!/bin/bash

#Multiplication table till 15

echo -n "Enter a number "
read number
n=1
until [ $n -gt 15 ]
do
	p=$[ $n*$number ]
	echo " $number*$n=$p"
	n=$[n+1]
done
