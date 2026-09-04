#!/bin/bash

#Sorting based on the height column

sort -t "," -k2,2 -n SOCR-HeightWeight_data.csv

#Check if the tallest person also weighs the most

sort -t "," -k2,2 -n -r SOCR-HeightWeight_data.csv > height_sort 

sort -t "," -k3,3 -n -r SOCR-HeightWeight_data.csv > weight_sort

head -1 height_sort ; head -1 weight_sort

echo "The tallest person is not the person that weighs the most"

