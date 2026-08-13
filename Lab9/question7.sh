#!/bin/bash


Energy=$(bc << EOF
mass=1
speed=3*10^8
mass*speed^2
EOF
)

echo "The calculated energy is $Energy"



