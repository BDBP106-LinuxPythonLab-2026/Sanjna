#!/bin/bash

echo -n "Input score (0-100)"
read score

if [ $score -ge 90 ]; then
	echo "A"
elif [ $score -lt 90 ] && [ $score -ge 80 ] ; then
	echo "B"
elif [ $score -lt 80 ] && [ $score -ge 70 ]; then
	echo "C"
else
	echo "Fail"
fi

