#!/bin/bash

echo "Input a number: "
read n
if [ "$n" -gt 100 ]; then
#delete additional "[" and change ")" to "]"
echo "The number is greater than 100."
else
echo "The number is not greater than 100."
fi
if [ "$n" -gt 100 ]; then
#delete additional "[" and "}" and add ";"
echo "The number is greater than 100."
fi
