#1/bin/bash

#To print even numbers between 0 and 50

n=0
while [ $n -lt 48 ]
do 
	n=$[n+2]
	echo $n
done

#Using a for loop

for i in {2..48..2}
do 
	echo $i
done
