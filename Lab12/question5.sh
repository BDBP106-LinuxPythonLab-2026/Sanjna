#!/bin/bash

echo "Enter dividend"
read dividend
echo "Enter divisor"
read divisor
function divide {
	local val1=$dividend
	local val2=$divisor

	if [ "$val2" == 0 ]; then
		echo "Error"
	fi

	local quotient=$(echo "scale=2;$val1/$val2" | bc)
	echo "The quotient is $quotient"
	local remainder=$[$val1%$val2]
	echo "The remainder is $remainder"
}

divide $dividend $divisor

