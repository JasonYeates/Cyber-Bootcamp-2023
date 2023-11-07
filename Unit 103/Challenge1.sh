#!/bin/bash

# Script Ops 201 Class 01 Ops Challenge Solution
# Author: Jason Yeates
# Date of latest revision: 11/06/2023
# Purpose: Print a string to the terminal


echo "hello $name"
name=$1
compliment=$2

user=$(whoami)
date=$(date)
whereami=$(pwd)
echo "goodmorning $name"
sleep 1
echo "nice face $name"
sleep 1
echo "you have a great $compliment"
sleep 2
echo "you are $user, your are in $whereami. today is $date"

