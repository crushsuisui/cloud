#!/bin/bash
#export.UTF-8
bt=$2
sjr=$1
FILE=/tmp/mailtmp.txt
echo "$3" >$FILE
/usr/bin/dos2unix -k $FILE
/bin/mail -s "$bt" "$sjr" <$FILE
