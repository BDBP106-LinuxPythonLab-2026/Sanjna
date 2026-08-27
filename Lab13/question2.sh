#!/bin/bash

#Print names of those who have scored less than 25

awk '$2<25 {print $0}' file2

#Print the student whose Physics score is given

awk '$3=="Physics" {print $0}' file2

#Rewrite data into csv format into a new file called data2.csv

awk '{printf "%6s, %3s, %10s\n" , $1, $2, $3}' file2 > data2.csv

