#!/bin/bash

val1=Jayashree
val2=Nagesh
#if [ $val1 > $val2 ]; then
#echo "$val1 is greater than $val2"
#else
#echo "$val1 is lesser than $val2"

if [ $val1 \> $val2 ]; then
echo "$val1 is greater than $val2"
else
echo "$val1 is lesser than $val2"
fi

# The latter script executes without creating a new file
# The escape character "\" treats the ">" as a greater than symbol instead of an output redirection operator

