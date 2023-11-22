#!/bin/bash
# Let's create an until loop that takes a variable and adds 1 till it reaches 10
# Have the script echo out what our current number is

x=1
until [ $x = 11 ]
do
    echo "x is $x"
    ((x++))
done
