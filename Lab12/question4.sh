#!/bin/bash

echo "2 3 5 7" > nums.txt
read -ra number < nums.txt
echo "The numbers in the array are: ${number[*]}"

for n in ${number[*]}
do
	product=$[$n*2]
	echo "The product of doubling $n is $product"
done
