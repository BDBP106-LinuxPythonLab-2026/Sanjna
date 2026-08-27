#!/bin/bash

#Remove header lines (containing >)

awk '!/>/' file3

#Convert to RNA seqeunce

sed 's/T/U/g' file3

#Replace seq1 by human_gene

sed 's/seq1/human_gene/' file3
