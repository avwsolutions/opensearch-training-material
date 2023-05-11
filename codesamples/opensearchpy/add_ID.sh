#!/bin/bash
IFS=$'\n' 
COUNTER=0
printf "Initial value of COUNTER=%d\n" $COUNTER

for x in `cat $1`
do
 echo $x
 echo "$COUNTER,$x" >> $1-refactored
 COUNTER=$(( COUNTER + 1 ))
done
