#!/bin/bash

echo "The value of home variable is: $HOME"

bcoutput=$(bc << EOF
scale=5
23934/44343
EOF
)
echo "23934/44343 gives $bcoutput"

lsoutput=$(ls /home/ibab | grep "D")
echo "The list of directories starting with D are: $lsoutput"

grep "ibab" /etc/passwd
