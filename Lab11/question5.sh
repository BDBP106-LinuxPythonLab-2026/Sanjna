#!/bin/bash

# (1)
var1=Testing
var2=testing

# (2)
if [ $var1 \> $var2 ]; then
	echo "$var1 is greater than $var2"
else
	echo "$var1 is lesser than $var2"
fi

# (3)
# The output is "Testing is lesser than testing"

# (4)
echo -e "$var1\n$var2" > teststringfile 

# (5)
sort "teststringfile"

#if statement output: "Testing' is lesser than "testing"
#in bash scripting the uppercase letters have lesser value then lowercase when comparing using standard ASCII comparisons
#sort output: "testing" is lesser than "Testing"
#standard sort sorts by alphabetical, lower case first
