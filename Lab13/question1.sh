#!/bin/bash


#Print the lines where the word and appears

sed -n '/and/p' file1

#Change all instances of language to lang

sed 's/language/lang/g' file1

#Delete lines containing the word 'is'

sed '/is/d' file1

#Insert line numbers

sed '=' file1 | sed 'N;s/\n/ /'

#Remove 1st 2 lines

sed '1,2d' file1

#Print every other line

sed -n '1~2p' file1

#Substitute first instance of 'Python' by 'python' and 'language' into 'lang'

sed 's/Python/python/;s/language/lang' file1


